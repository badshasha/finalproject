from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib.auth import login as auth_login  # because i already have got log in function
from django.contrib.auth import logout as auth_logout # because i have got logout function
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.admin import User

from adminController.models import RecordLogin  # working not a error
from .custom_class.subject_selector import SubjectSelection # subject class import
from .custom_class.Validator import  Validation
from .models import  StudentsSubject , PicProfile
from subjects.models import  Subjects ,SubTopic , Exam # this error not error it's pychart issue [not a real one]
from django.http import JsonResponse  # handling json infomation
from django.core import serializers
from math import floor
import random


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def loadMain(request):
    return render(request, "mainpage/homepage.html")


def login(request):
    if request.method == 'POST':
        # print(f"{request.POST['name']}   password is {request.POST['password']}")
        found_user = authenticate(username=request.POST['name'], password=request.POST['password'])
        if found_user is not None:

            new_record = RecordLogin.objects.create(user_id=found_user.pk, ip=get_client_ip(request), status=1)
            new_record.save()
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
                subject_table = StudentsSubject.objects.create(student_id=new_user) # student subject profile creating
                subject_table.save() # add user subject table
                pic_profile =  PicProfile.objects.create(user_profile=new_user)  # pic profile
                pic_profile.save()

                print("working")
                return redirect('login')
            except  IntegrityError:
                error = "entered name exists on the system "
        else:
            error = 'wrong infomation please check your information again '
    return render(request, "mainpage/login.html", {'error': error})


def logout(request,id):
    if request.method == 'POST':
        new_record = RecordLogin.objects.create(user_id=id, ip=get_client_ip(request), status=0)
        new_record.save()
        auth_logout(request)
        return redirect('indexpage') # homepage name


def userDashBroard(request):
    # if request.user:  need to update this part
    try:
        logged_time=request.user.last_login
        print(logged_time)
        return render(request, 'mainpage/userdash.html',{'logtime':logged_time})
    except :
        return redirect('login')


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
    # print([len(subject.subtopic_set.all()) for subject in selected_subjects])
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
        'subtopic': serialized_qs
    }

    return JsonResponse(data)

# selected exam page


def examsubtopicpage(request,id):
    subject_selector_instance = SubjectSelection()
    simple = subject_selector_instance.getSample(id, 5)  # class creating
    return render(request, 'mainpage/questionpaper.html', {'paper': simple, 'full': False})


def testingPost(request):
    if request.POST:
        subject_selector_instance = SubjectSelection()
        v = Validation()
        token_pass = 0
        question = None
        # read input and calculate percentage
        for key, value in request.POST.items():
            if token_pass == 0:
                token_pass += 1
                continue
            if 'full_paper' == key:
                continue
            print(f'{key} {value}')
            question = subject_selector_instance.getQuesion(key)
            print(question)
            v.checkAnswer(question, value)
            token_pass += 1

        # print(v.getResult())
        # print(v.Percentage_of_success())
        # print(v.Percentage_of_failier())
        # print(question.subject_name)
        # print(request.user)
        if  request.POST["full_paper"] == "False":
            exam = Exam.objects.create(user=request.user,subject=question.subject_name,success= v.Percentage_of_success(),fail=v.Percentage_of_failier())
            print("page informatino store success [++++++]")
            exam.save()
        else:
            # print(request.POST["full_paper"])
            print(" full page loading if not check the statement  ")

        # update database based on user information

        # return response
        return render(request,'mainpage/resultPage.html', {'paper': v.getResult(),'success': v.Percentage_of_success(), 'fail' : v.Percentage_of_failier()})
    return HttpResponse(request.POST);


# get request user selected page
def getExamResult(request):
    list_of_subjects = request.user.studentssubject.subjects.all()
    # print(list_of_subjects)
    return render(request,'mainpage/examchart.html', {'subjects': list_of_subjects})

# get subject chart info
def getSubjectChart(request,id):
    subject = Subjects.objects.filter(id=id).first()
    queryset = subject.subtopic_set.all()
    serialized_qs = serializers.serialize('json', queryset)
    data = {
        #
        'subtopic': serialized_qs
    }

    return JsonResponse(data)

def examsubjectjson(request):
    pass


def getChart(request,id):
    subtopic = SubTopic.objects.filter(id=id).first()
    mark_info =request.user.exam_set.filter(subject=subtopic).order_by('date')
    data = serializers.serialize('json', mark_info)
    data_list = {
        'marks': data
    }

    return JsonResponse(data_list)


def fullpaper(request,id):
    question_papaer_size = 10
    selected_subject=Subjects.objects.filter(id=id).first()
    subtopic_list = selected_subject.subtopic_set.all()
    # print(subtopic_list)
    last_record_info = [request.user.exam_set.filter(subject=value).order_by('date').first() for value in subtopic_list]
    if None in last_record_info:
        values = last_record_info.index(None)
        return render(request, 'mainpage/examRequestError.html',{"subject":subtopic_list[values]})

    get_presentages = [value.fail if value.fail > 0 else value.fail+1 for value in last_record_info ]
    get_ratio = [ vaule/min(get_presentages) for vaule in get_presentages]

    final_paper = [ floor(value/sum(get_ratio) * question_papaer_size) for value in get_ratio]
    diff = question_papaer_size - sum(final_paper)
    min_value_position = final_paper.index(min(final_paper))
    final_paper[min_value_position] = min(final_paper) + diff

    # question selection
    simple = None
    question_class = SubjectSelection()
    for subtopic , count in zip(subtopic_list,final_paper):
        simple = question_class.getSample(subtopic.id,count)
        # print(f'{subtopic.id}  {count}')

    return render(request, 'mainpage/questionpaper.html', {'paper': simple , 'full':True})
    # return HttpResponse(f"{question_list[-1]}")



def updateUser(request):
    if request.method == "POST":
        # if  request.POST["username"]:
        #     username = request.POST["username"].strip()
        #     request.user.username = username
        #     request.user.save()
        if  request.POST["f_name"]:
            f_name = request.POST["f_name"].strip()
            request.user.first_name = f_name
            request.user.save()

        if  request.POST["l_name"]:
            l_name = request.POST["l_name"].strip()
            request.user.last_name = l_name
            request.user.save()
        return redirect('userdashbord')

        # print(username,f_name,l_name,sep='\n')



    return render(request,'mainpage/userupdate.html')
