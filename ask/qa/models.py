from django.db import models
from django.contrib.auth.models import User

# some sort of changes for get in stepik test


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    # added_at = models.DateField(blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, default=1)
    likes = models.ManyToManyField(
        User, related_name='liked_questions', blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/' + str(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               blank=True, null=True)

    def __unicode__(self):
        return self.text
