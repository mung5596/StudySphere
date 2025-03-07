from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from studygroup.models import StudyGroup
from question.models import Question


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = UserForm()
    return render(request, "signup.html", {"form": form})


def mypage(request):
    studygroup_list = StudyGroup.objects.all().order_by("-date")
    question_list = Question.objects.all().order_by("-create_date")
    context = {"studygroup_list": studygroup_list, "question_list": question_list}
    return render(request, "mypage.html", context)
