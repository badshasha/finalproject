from django.shortcuts import render,redirect,get_object_or_404
from .models import Subjects , SubTopic , Question , Answers , OtherAnswer
from .forms import SubjectForms , SubTopicForm,  QuestonForm , QuestionAddFrom , OtherAnswerUpdateForm , OtherAnswerAddFrom
from django.http import HttpResponse


def something(request):
    subjects_info = Subjects.objects.all()
    return render(request,'subjects/subject_all.html',{'subjects_info':subjects_info})


def addsubject(request):
    form = SubjectForms()
    if request.method == 'POST':
        newSubject = SubjectForms(request.POST)
        if newSubject.is_valid():
            newSubject.save()
            return redirect("subject")

    return render(request, 'subjects/useradd.html',{'subject_form':form})


def deleteSubject(request,subject_id):
    print("working")
    subject = get_object_or_404(Subjects,id=subject_id)
    if request.method == "GET":
        return render(request , 'subjects/deletesub.html',{'subject':subject})
    else:
        if "yes" in request.POST:
            subject.delete()
        return redirect("subject")

def subjectUpdate(request,subject_id):
    subject = get_object_or_404(Subjects,id=subject_id)
    if request.method == 'GET':
        form = SubjectForms(instance=subject)

    else:
        form = SubjectForms(request.POST,instance=subject)
        if form.is_valid():
            form.save()
            return redirect("subject")

    return render(request,'subjects/subjectupdate.html',{'subject_info':form,'subject':subject})



# subtopic controller

def subtopic(request,subject_id):
    info =SubTopic.objects.filter(subject=subject_id) # foregin key column
    return render(request,'subjects/subtopic.html',{'subtopic_info':info,'subject_id':subject_id})


def addsubtopic(request,subject_id):
    form = SubTopicForm()
    if request.method == "GET":
        subject = get_object_or_404(Subjects,id=subject_id)
        return render(request,'subjects/subtopicAdd.html',{'form':form,'subject':subject})
    else:
        print(request.POST)
        form = SubTopicForm(request.POST)
        if form.is_valid():
            print("working$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            form.save()
            return redirect('subtopic',subject_id)


def subtopicupdate(request,subtopic_id):
    subtopic = get_object_or_404(SubTopic,id=subtopic_id)
    if request.method == "GET":
        return render(request, 'subjects/subtopicupdate.html',{'subtopic':subtopic})
    else:
        form = SubTopicForm(request.POST,instance=subtopic)
        print(request.POST)
        if form.is_valid():
            print("---------------------------------------------------------------------------------------------------")
            form.save()
            return redirect('subtopic',subtopic.subject.id)
        # return render(request, 'subjects/subtopicupdate.html',{'subtopic':subtopic})


def subtopicdelete(request,subtopic_id):
    subtopic = get_object_or_404(SubTopic,id=subtopic_id)
    # info = SubTopic.objects.filter(id=subtopic_id)[0]
    if request.method == "GET":
         return render(request,'subjects/subtopicdelete.html',{'subtopic':subtopic})
    else:
         if "yes" in request.POST:
             print(subtopic.subject.id)
             subtopic.delete()
             return redirect('subtopic',subtopic.subject.id)


######################################################################
############# quesiton handling ###########################################

def question(request,subtopic_id):
    info = Question.objects.filter(subject_name=subtopic_id)
    return render(request,'subjects/question.html',{'questions':info,'qustion_id':subtopic_id})

def updatequeston(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    # form = QuestonForm()
    if request.method == "GET":
        return render(request,'subjects/updatequestion.html',{'question_info':question})
    else:
        form = QuestonForm(request.POST,instance=question)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question',question.subject_name.id)

def deletequeston(request,question_id):
    question = get_object_or_404(Question,id=question_id)
    if request.method == "GET":
        return render(request,"subjects/deletequestion.html",{'question':question})
    else:
        if "yes" in request.POST:
            question.delete()
        return redirect('question',question.subject_name.id)

def addquestion(request,question_id):
    form = Question()
    if request.method == "GET":
        subtopic_info = get_object_or_404(SubTopic,id=question_id)
        return render(request, "subjects/questionadd.html" , {'form':form , 'subject_info':subtopic_info})
    else:
        print(request.POST)
        form = QuestionAddFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question',question_id)

        return HttpResponse(form)
        # if form.is_valid():
        #     print("working--------------------")

##########################################################
################# random other answer ####################


def random_answer(request,question_id):
    other_answers = OtherAnswer.objects.filter(question=question_id)
    print(f'############################################{other_answers}')
    return render(request,'subjects/other_answer.html',{'other_answers': other_answers,"question_id":question_id})


def random_answer_update(request,other_answer_id):
    other_answer_finder = get_object_or_404(OtherAnswer, id=other_answer_id)

    if request.method == "GET":
        # form = OtherAnswerUpdateForm(other_answer_finder)
        return render(request,'subjects/otherquesitonupdate.html', {'info': other_answer_finder})
    else:

        form = OtherAnswerUpdateForm(request.POST, instance=other_answer_finder)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otherquestion', other_answer_finder.question.id )
        return HttpResponse("invalid")


def random_answer_add(request,question_id):
    Q = Question.objects.filter(id=question_id).first()
    form = OtherAnswerUpdateForm()
    print(Q)
    if request.method == "GET":
        return render(request,'subjects/addotheranswer.html',{'form':form,'question_id':Q})
    else:
        print(request.POST)
        update_request = request.POST.copy()
        update_request.update({'question':question_id})
        print(update_request)
        #form = OtherAnswerUpdateForm(request.POST)
        form = OtherAnswerAddFrom(update_request)
        if form.is_valid():
            form.save()
            return redirect('otherquestion', question_id )
        return render(request,'subjects/addotheranswer.html',{'form':form,'question_id':Q})

def random_anwer_delete(request,question_id):
    other_anser = get_object_or_404( OtherAnswer , id=question_id )
    if request.method == "GET":
        return render(request,'subjects/deleteotheranswer.html',{'info' : other_anser})
    else:
        if "yes" in request.POST:
            other_anser.delete()
        return redirect('otherquestion', other_anser.question.id )
