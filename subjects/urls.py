from django.urls import path
from . import views

urlpatterns = [
    path("", views.something, name="subject"),
    path("addsubject/", views.addsubject, name='addsubjectpage'),
    path('deletesubject/<int:subject_id>/', views.deleteSubject, name='deletesubject'),
    path('subjectupdate/<int:subject_id>/', views.subjectUpdate, name='subjectupdate'),
    path('subtopic/<int:subject_id>', views.subtopic, name='subtopic'),
    path('addsubtopic/<int:subject_id>', views.addsubtopic, name='addsubtopic'),
    path('updatesubtopic/<int:subtopic_id>', views.subtopicupdate, name='subtopicupdate'),
    path('deletesubtopic/<int:subtopic_id>', views.subtopicdelete, name='subtopicdelete'),
    path('question/<int:subtopic_id>', views.question, name='question'),
    path('updatequeston/<int:question_id>', views.updatequeston, name='updatequeston'),
    path('deletequestion/<int:question_id>', views.deletequeston, name='deletequeston'),
    path('addqusetion/<int:question_id>', views.addquestion, name='addquestion'),
    path('otheranswer/<int:question_id>',views.random_answer,name='otherquestion'), # name wrong
    path('otheranswerupdate/<int:other_answer_id>', views.random_answer_update, name="otheranswerupdate"),
    path('otheransweradd/<int:question_id>', views.random_answer_add, name='otheransweradd'),
    path('otheranswerdelete/<int:question_id>' , views.random_anwer_delete ,name = 'otheranswerdelete')

]
