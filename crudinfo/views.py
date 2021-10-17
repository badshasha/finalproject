from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
# from .forms import FromUserCreate


class UserInfoInder:
    @staticmethod
    def findUser(user_id):  # reade user model and find user
        return  get_object_or_404(User,id=user_id)


def homepage(request):  # [+] render all user form
    user = User.objects.all()  # read all row
    return render(request,'crudInfo/home.html',{"user":user})


def userPage(request,user_id):

    user_variable = get_object_or_404(User,id=user_id)

    if request.method == 'POST':
        print("user request working")
        print(user_variable)
        form = UserChangeForm(request.POST, instance=user_variable)
        if form.is_valid():
            print("page is valid")
            form.save()
            print("page save success")
            return redirect('homepage')
    # else:

    form = UserChangeForm(instance=user_variable)
    # form = FromUserCreate()
    return render(request,"crudInfo/userpage.html",{"user":user_variable,"form":form})


def deleteUser(request,user_id):

    u = UserInfoInder.findUser(user_id) # find the user
    if request.method == 'GET':
        return render(request , 'crudInfo/delete.html',{'user':u})
    else:
        if "yes" in request.POST:
            u.delete()

        return redirect('homepage')


def addUser(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            #  need some message
        else:
            return render(request,'crudInfo/addUser.html',{'form':form})

        return redirect('homepage')
    else:
        form = UserCreationForm() # create new object
        return render(request,'crudInfo/adduser.html',{'form':form})
