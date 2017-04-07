from rest_framework import serializers
from .models import Question, Answer, QuestionComment, AnswerComment, Tag, QuestionVote, AnswerVote, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'title', 'text', 'created', 'modified', 'user')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'created', 'modified', 'question_id', 'user_id', 'is_accepted_answer')


class QuestionCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ('id', 'user_id', 'question_id', 'text', 'created')


class AnswerCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerComment
        fields = ('id', 'user_id', 'answer_id', 'text', 'created')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'text', 'question_id')


class QuestionVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionVote
        fields = ('id', 'user_id', 'question_id', 'is_upvote')


class AnswerVoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerVote
        fields = ('id', 'user_id', 'answer_id', 'is_upvote')
