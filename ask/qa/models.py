from django.db import models

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

