# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    topics = models.ManyToManyField("Topic")

    def __str__(self):
        return self.topic

class Topic(models.Model):
    topic = models.CharField(max_length=80)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.topic

class Answer(models.Model):
    body = models.TextField()
    question = models.ForeignKey(
        Question, blank=True, null=True, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.topic

class Testhistory(models.Model):
    body = models.TextField()
    topic = models.CharField(max_length=80)
    score = models.IntegerField()

    def __str__(self):
        return self.topic




    


