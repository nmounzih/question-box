from rest_framework import serializers
from .models import Question, Answer, QuestionComment, AnswerComment, Tag, QuestionVote, AnswerVote, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'text', 'created', 'modified', 'user_id')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'created', 'modified', 'question_id', 'user_id', 'is_accepted_answer')


class QuestionCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('user_id', 'question_id', 'text', 'created')


class AnswerCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerComment
        fields = ('user_id', 'answer_id', 'text', 'created')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('text', 'question_id')


class QuestionVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionVote
        fields = ('user_id', 'question_id', 'is_upvote')


class AnswerVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerVote
        fields = ('user_id', 'answer_id', 'is_upvote')
