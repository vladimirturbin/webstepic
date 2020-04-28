from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='liked_questions')

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.text

<<<<<<< HEAD
=======
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    ratings = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.text

>>>>>>> 951bece4f8b9e8e7ea72b843d33258a121c022a2
