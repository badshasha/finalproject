from django.shortcuts import render

# Create your views here.

def adminHomepage(request):
    return render(request,'adminController/homepage.html')
