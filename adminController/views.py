from django.shortcuts import render
from subjects.models import Subjects
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.template import  RequestContext

# Create your views here.




def adminHomepage(request):
    subject = Subjects.objects.all()
    return render(request,'adminController/homepage.html',{'short_cut':subject})

# json responce
def subjectInfo(request):
    subject = Subjects.objects.all()
    responseData = {
     'label':[ value.name for value in subject],
     'data': [len(subject.subtopic_set.all()) for subject in subject],
     'count': subject.count()
    }
    return JsonResponse(responseData)

def userinfo_json(request):
    users = User.objects.all()
    supper_user = []
    normal_user = []
    for u in users:
        if u.is_superuser == True:
            supper_user.append(u)
        else:
            normal_user.append(u)

    responseData = {
        'label':['admin privilage','user privilage'],
        'data' : [len(supper_user) , len(normal_user)]
    }
    return JsonResponse(responseData)




# def currentUser(request):
#     count = User.objects.filter(last_login__startswith=timezone.now().date()).coun
#     ...: t()