from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    # Q&A functionality
    path("", views.question, name="question"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("create/", views.create_question, name="create_question"),
    path("<int:question_id>/create/", views.create_answer, name="create_answer"),
]
