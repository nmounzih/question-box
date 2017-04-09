from django.shortcuts import render, HttpResponse, redirect
from rest_framework import viewsets
from .models import Question, Answer, QuestionComment, AnswerComment, Tag, QuestionVote, AnswerVote
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, AnswerSerializer, QuestionCommentSerializer, AnswerCommentSerializer, UserSerializer, TagSerializer, QuestionVoteSerializer, AnswerVoteSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('created')
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Answer.objects.all().order_by('created')
    serializer_class = AnswerSerializer


class QuestionCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = QuestionComment.objects.all().order_by('created')
    serializer_class = QuestionCommentSerializer


class AnswerCommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = AnswerComment.objects.all().order_by('created')
    serializer_class = AnswerCommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class QuestionVoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = QuestionVote.objects.all()
    serializer_class = QuestionVoteSerializer


class AnswerVoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = AnswerVote.objects.all()
    serializer_class = AnswerVoteSerializer


def index(request):
    context = {}
    all_questions = Question.objects.all()
    for question in all_questions:
        question.score = len(question.questionvote_set.filter(is_upvote=True)) - len(question.questionvote_set.filter(is_upvote=False))
        question.num_answers = len(Answer.objects.filter(question_id=question.id))
        question.save()
    all_questions = Question.objects.order_by('-created')
    context['all_questions'] = all_questions
    return render(request, 'question_box_app/index.html', context)


def profile(request, user_id):
    score = 0
    downvotes = len(AnswerVote.objects.filter(user_id=user_id, is_upvote=False)) + len(QuestionVote.objects.filter(user_id=user_id, is_upvote=False))
    answers = Answer.objects.filter(user_id=user_id)
    questions = Question.objects.filter(user_id=user_id)
    context = {'questions': questions, 'answers': answers, 'user_id': user_id, 'username': User.objects.get(id=user_id).username}
    for answer in answers:
        score += len(answer.answervote_set.filter(is_upvote=True)) * 10 - len(answer.answervote_set.filter(is_upvote=False)) * 5 + 5*len(questions) - downvotes
    context['score'] = score
    context['num_questions'] = len(questions)
    context['num_answers'] = len(answers)
    return render(request, 'question_box_app/profile.html', context)


def question_detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    q.num_views += 1
    q.score = len(q.questionvote_set.filter(is_upvote=True)) - len(q.questionvote_set.filter(is_upvote=False))
    q.save()
    answers = q.answer_set.filter(question_id=question_id)
    context = {'answers': []}
    context['question'] = q
    context['username'] = User.objects.get(id=q.user_id)
    context['num_answers'] = len(answers)
    context['user_id'] = request.user.id
    for a in answers:
        a.score = len(a.answervote_set.filter(is_upvote=True)) - len(a.answervote_set.filter(is_upvote=False))
        a.save()
        context['answers'].append(a)
    return render(request, 'question_box_app/question_detail.html', context)
    # return HttpResponse('QID: {} Title: {} Score: {}, Answers: {}'.format(q.id, q.title, score, context))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
