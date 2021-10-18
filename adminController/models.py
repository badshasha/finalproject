from django.db import models
from django.contrib.auth.models import  User
import datetime

# Create your models here.

class RecordLogin(models.Model):
    user_id = models.IntegerField()
    # datetime = models.DateTimeField(auto_now=True)
    ip = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    status = models.IntegerField() # if 1 then log in 0 then log out from the system

    def __str__(self):
        return f'{self.user_id} {self.date} {self.status}'

