from django.contrib import admin
from .models import Question, Answer, Topic, Testhistory

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
admin.site.register(Testhistory)
