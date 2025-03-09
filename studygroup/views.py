from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from services import send_email


def studygroup(request):
    studygroup_list = StudyGroup.objects.all().order_by("-date")
    context = {"studygroup_list": studygroup_list}
    return render(request, "studygroup.html", context)


def create_studygroup(request):
    if request.user.is_anonymous:
        messages.warning(request, "Please login or sign up first")
        return redirect("studygroup")
    if request.method == "POST":
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            new_studygroup = form.save(commit=False)
            new_studygroup.creator = request.user
            new_studygroup.save()
            new_studygroup.participants.add(request.user)
            new_studygroup.save()
            return redirect("studygroup")
    else:
        form = StudyGroupForm()
    context = {"form": form}
    return render(request, "create_studygroup.html", context)


def join_studygroup(request, group_id):
    # when user is not logged in
    if request.user.is_anonymous:
        messages.warning(request, "Please login or sign up first")
        return redirect("studygroup")

    # fetch the study group
    study_group = StudyGroup.objects.get(id=group_id)

    # when study group is full
    if study_group.current_people >= study_group.max_people:
        messages.warning(request, "This study group is already full.")
        return redirect("studygroup")

    # update the study group
    study_group.participants.add(request.user)
    study_group.current_people += 1
    study_group.save()

    messages.success(request, "You have successfully joined the study group!")

    # send email
    subject = f"Update to your {study_group.name} study group"
    body = (
        f"{request.user.first_name} {request.user.last_name} has joined your {study_group.name} study group. You "
        f"now have {study_group.current_people} out of {study_group.max_people} in your study group. "
    )
    recipient_list = [study_group.creator.email]
    send_email(subject, body, recipient_list)

    return redirect("studygroup")


def leave_studygroup(request, group_id):
    study_group = StudyGroup.objects.get(id=group_id)
    study_group.participants.remove(request.user)
    study_group.current_people -= 1
    study_group.save()
    messages.success(request, "You have successfully left the study group")

    # send email
    subject = f"Update to your {study_group.name} study group"
    body = (
        f"{request.user.first_name} {request.user.last_name} has left your {study_group.name} study group. You "
        f"now have {study_group.current_people} out of {study_group.max_people} in your study group. "
    )
    recipient_list = [study_group.creator.email]
    send_email(subject, body, recipient_list)

    return redirect("studygroup")


def cancel_studygroup(request, group_id):
    study_group = StudyGroup.objects.get(id=group_id)
    study_group.status = "CA"
    study_group.save()

    messages.success(request, "You have successfully cancelled the study group")

    # send email
    subject = f"{study_group.name} study group is cancelled"
    body = f"This email has been sent to inform you that {study_group.name} study group has been cancelled by the owner. "
    recipient_list = []
    for participant in study_group.participants.all():
        recipient_list.append(participant.email)
        print(recipient_list)
    send_email(subject, body, recipient_list)

    return redirect("studygroup")


def complete_studygroup(request, group_id):
    study_group = StudyGroup.objects.get(id=group_id)
    study_group.status = "CO"
    study_group.save()

    messages.success(request, "You have successfully completed the study group")

    return redirect("studygroup")
