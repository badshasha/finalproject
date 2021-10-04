from django import forms
from .models import Subjects, SubTopic, Question, Answers, OtherAnswer


class SubjectForms(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class': 'say_hello'})  # suppppppper bad
        # }


class SubTopicForm(forms.ModelForm):
    class Meta:
        model = SubTopic
        fields = "__all__"


class QuestonForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'correct_answer']


class QuestionAddFrom(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class OtherAnswerUpdateForm(forms.ModelForm):
    class Meta:
        model = OtherAnswer
        fields = ['other_ansewr']


class OtherAnswerAddFrom(forms.ModelForm):
    class Meta:
        model = OtherAnswer
        fields = "__all__"
