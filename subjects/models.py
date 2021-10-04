from django.db import models

# Create your models here.

class Subjects(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'subject {self.name}'

class SubTopic(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.subject.name} => {self.name}'


class Question(models.Model):
    question = models.CharField(max_length=100)
    subject_name = models.ForeignKey(SubTopic,on_delete=models.CASCADE,null=True)
    correct_answer = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.question}'

# wrong clsses
class Answers(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.answer}'


class OtherAnswer(models.Model):
    other_ansewr = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.other_ansewr} comes under {self.question.question}'
