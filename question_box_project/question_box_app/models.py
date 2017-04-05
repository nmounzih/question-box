from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.__repr__()


class Answer(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_accepted_answer = models.BooleanField(default=False)

    def __repr__(self):
        return self.text[:50]

    def __str__(self):
        return self.__repr__()


class QuestionComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.text[:50]

    def __str__(self):
        return self.__repr__()


class AnswerComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.text[:50]

    def __str__(self):
        return self.__repr__()


class Tag(models.Model):
    text = models.CharField(max_length=100)
    question = models.ManyToManyField(Question)

    def __repr__(self):
        return self.text

    def __str__(self):
        return self.__repr__()


class QuestionVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    def __repr__(self):
        return '{} {}'.format(self.question.title, self.is_upvote)

    def __str__(self):
        return self.__repr__()


class AnswerVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_upvote = models.BooleanField()

    def __repr__(self):
        return '{} {}'.format(self.answer.text[:50], self.is_upvote)

    def __str__(self):
        return self.__repr__()
