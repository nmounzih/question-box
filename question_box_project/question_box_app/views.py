from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import Question, Answer, QuestionComment, AnswerComment, Tag, QuestionVote, AnswerVote
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, AnswerSerializer, QuestionCommentSerializer, AnswerCommentSerializer, UserSerializer, TagSerializer, QuestionVoteSerializer, AnswerVoteSerializer


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
    return HttpResponse('index')


def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    return HttpResponse('profile: {}'.format(user))


def question_detail(request, question_id):
    q = Question.objects.get(pk=question_id)

    score = len(q.questionvote_set.filter(is_upvote=True)) - len(q.questionvote_set.filter(is_upvote=False))
    answers = q.answer_set.filter(question_id=question_id)

    context = {}
    for a in answers:
        context[a.id] = str(a.text)

    return HttpResponse('QID: {} Title: {} Score: {}, Answers: {}'.format(q.id, q.title, score, context))
