from django.contrib import admin
from .models import Subjects , SubTopic,Question,Answers,OtherAnswer

# Register your models here.

admin.site.register((Subjects,SubTopic,Question,Answers,OtherAnswer))
