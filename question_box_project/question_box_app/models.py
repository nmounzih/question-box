from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    score = models.IntegerField()
    user = models.OnetoOneField(User, on_delete=models.CASCADE)


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)


class Answer(models.Model):
    text = models.TextField()
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    accepted_answer = models.BooleanField(default=False)


class QuestionComment:
    user = models.ForeignKey(Profile)
    question = models.ForeignKey(Question)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class AnswerComment:
    user = models.ForeignKey(Profile)
    answer = models.ForeignKey(Answer)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)


class Tag:
    text = models.CharField(max_length=100)
    question = models.ManyToManyField(Question)
