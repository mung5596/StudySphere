from django.urls import path
from . import views

urlpatterns = [
    path("", views.question, name="question"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("create/", views.create_question, name="create_question"),
    path("<int:question_id>/create/", views.create_answer, name="create_answer"),
]
