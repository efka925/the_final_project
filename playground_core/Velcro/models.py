from django.db import models
from django.db.models import User

# Create your models here.
class Questions(models.Model):
    topic = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.topic 
    

class Answer(models.Model):
    topic = models.CharField(max_length=80)
    body = models.TextField()
    
    def __str__(self):
        return self.topic

