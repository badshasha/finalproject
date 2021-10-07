from django.db import models
from django.contrib.auth.models import User
from subjects.models import  Subjects # dont worry this thing is working 'pycharm error not the sytem'

# Create your models here.

class StudentsSubject(models.Model):
    student_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    subjects = models.ManyToManyField(Subjects)

    def __str__(self):
        return f'{ self.student_id.username } selected { len(self.subjects.all())} subjects'

