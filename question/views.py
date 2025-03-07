from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils import timezone
from .forms import *
from services import send_email


def question(request):
    question_list = Question.objects.all().order_by("-create_date")
    context = {"question_list": question_list}
    return render(request, "question.html", context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "question_detail.html", context)


def create_question(request):
    if request.user.is_anonymous:
        messages.warning(request, "Please login or sign up first")
        return redirect("question")
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.creator = request.user
            new_question.create_date = timezone.now()
            new_question.save()
            return redirect("question")
    else:
        form = QuestionForm()
    context = {"form": form}
    return render(request, "create_question.html", context)


def create_answer(request, question_id):
    if request.user.is_anonymous:
        messages.warning(request, "Please login or sign up first")
        return redirect("detail", question_id=question_id)

    question = Question.objects.get(id=question_id)
    answer = Answer(
        creator=request.user,
        question=question,
        content=request.POST.get("content"),
        create_date=timezone.now(),
    )
    answer.save()

    # send email
    subject = f"Answer added to your {question.title} question"
    body = f"{request.user.first_name} {request.user.last_name} has left a new answer to your {question.title} \
question. Click 127.0.0.1:8000/question/{question_id}/ to check the update."
    recipient_list = [question.creator.email]
    send_email(subject, body, recipient_list)

    return redirect("detail", question_id=question_id)
