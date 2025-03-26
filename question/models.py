from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
