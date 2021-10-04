from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import login as auth_login  # because i already have got log in function
from django.contrib.auth import logout as auth_logout # because i have got logout function
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.admin import User

from .custom_class.subject_selector import SubjectSelection # subject class import
from .custom_class.Validator import  Validation
from .models import  StudentsSubject
from subjects.models import  Subjects ,SubTopic # this error not error it's pychart issue [not a real one]
from django.http import JsonResponse  # handling json infomation
from django.core import serializers
import random



def loadMain(request):
    return render(request, "mainpage/homepage.html")


def login(request):
    if request.method == 'POST':
        # print(f"{request.POST['name']}   password is {request.POST['password']}")
        found_user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if found_user is not None:
            auth_login(request, found_user)  # django login function
            return redirect('userdashbord')
    return render(request, "mainpage/signin.html")


def singin(request):
    error = ""
    if request.method == 'POST':
        if request.POST['f_name'] != '' and request.POST['email'] and (request.POST['password1']==request.POST['password2'] ):
            try:
                new_user = User.objects.create_user(username=request.POST['f_name'], email=request.POST['email'], password=request.POST['password1'])
                new_user.save() # save user
                subject_table = StudentsSubject.objects.create(student_id=new_user)
                subject_table.save() # add user subject table

                print("working")
                return redirect('login')
            except  IntegrityError:
                error = "entered name exists on the system "
        else:
            error = 'wrong infomation please check your information again '
    return render(request, "mainpage/login.html",{'error':error})


def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('indexpage') # homepage name


def userDashBroard(request):
    # if request.user:

    return render(request, 'mainpage/userdash.html')


def userDashBrod_selectedsub(request):  # selecet_subject
    student_subject = request.user.studentssubject.subjects.all()
    return render(request, 'mainpage/selectsubject.html', {'subject': student_subject})


def addusersubject(request):  # name =>  adduser_subject

    if request.method == 'POST':
        selected_subject = request.POST['select_subject']
        subject_object = Subjects.objects.filter(id=selected_subject).first()
        print(subject_object)
        request.user.studentssubject.subjects.add(subject_object)

    student_subject = request.user.studentssubject.subjects.all()
    values =Subjects.objects.all()

    student_current_subjects = values.intersection(student_subject)
    unselected_subjects = values.difference(student_subject)
    print(unselected_subjects)
    return render(request,'mainpage/addnewsubject.html',{'select':student_current_subjects,'un_select':unselected_subjects})


def removeusersubject(request,id):
    value = request.user.studentssubject.subjects.filter(id=id).first()
    request.user.studentssubject.subjects.remove(value)
    return redirect( 'selecet_subject')



################################################################################################
# exam controlling function
def exampage(request):
    # subject = request.user.studentssubject.subjects.all().first();
    # subtopics = subject.subtopic_set.all()
    # main = []
    # for subtopic in subtopics:
    #     sub = []
    #     for v in subtopic.question_set.all():
    #         temp = {}
    #         temp["question"] = v.question
    #         temp["answer"] = v.correct_answer
    #         temp["wrong"] = [ other_answer_object.other_ansewr for other_answer_object in v.otheranswer_set.all()]
    #
    #         sub.append(temp)
    #     main.append(sub)
    # print(len(main[0]))
    # print(len(main))

    subject = request.user.studentssubject.subjects.all()
    return render(request, 'mainpage/exampage.html', {'subject': subject})





############################ json #############################################################
################################################################################################
# send subject info  (select subject and non selected subjects )
def json(request):
    selected_subjects = request.user.studentssubject.subjects.all();
    full_subject = Subjects.objects.all();
    unselected_subjects = full_subject.difference(selected_subjects)

    responseData = {
        'label': ['unselected subject','selected subject'],
        'data': [len(unselected_subjects), len(selected_subjects)]
    }
    return JsonResponse(responseData)

# show all the information about subject and subsubjects
def json_subject(request):
    selected_subjects = request.user.studentssubject.subjects.all();
    # print(set(selected_subjects))
    # print([values.name for values in selected_subjects])
    # print([values.subtopic for values in selected_subjects])
    #  print([    len(subject.subtopic_set.all()) for subject in selected_subjects ])
    responseData = {

        'label': [values.name for values in selected_subjects],
        'data': [len(subject.subtopic_set.all()) for subject in selected_subjects]
    }
    return JsonResponse(responseData)

# json file
def examsubtopic(request,id):
    subject = Subjects.objects.filter(id=id).first()
    queryset = subject.subtopic_set.all()
    serialized_qs = serializers.serialize('json', queryset)
    data = {
        #
        'subtopic' : serialized_qs
    }

    return JsonResponse(data)

# selected exam page


def examsubtopicpage(request,id):
    subject_selector_instance = SubjectSelection()
    simple = subject_selector_instance.getSample(id,5) # class creating
    return render(request,'mainpage/questionpaper.html',{'paper':simple})

def testingPost(request):

    if request.POST:
        subject_selector_instance = SubjectSelection()
        v = Validation()
        token_pass = 0

        # read input and calculate percentage
        for key, value in request.POST.items():
            if token_pass == 0:
                token_pass += 1
                continue
            v.checkAnswer(subject_selector_instance.getQuesion(key),value)
            token_pass += 1
        # print(v.getResult())
        # print(v.Percentage_of_success())
        # print(v.Percentage_of_failier())

        # update database based on user information

        # return response
        return render(request,'mainpage/resultPage.html', {'paper': v.getResult(),'success': v.Percentage_of_success(), 'fail' : v.Percentage_of_failier()})
    return HttpResponse(request.POST);
