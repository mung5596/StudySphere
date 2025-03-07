from django.urls import path
from . import views

urlpatterns = [
    path("", views.studygroup, name="studygroup"),
    path("create/", views.create_studygroup, name="create_studygroup"),
    path("<int:group_id>/join/", views.join_studygroup, name="join_studygroup"),
    path("<int:group_id>/leave/", views.leave_studygroup, name="leave_studygroup"),
    path("<int:group_id>/cancel/", views.cancel_studygroup, name="cancel_studygroup"),
    path(
        "<int:group_id>/complete/",
        views.complete_studygroup,
        name="complete_studygroup",
    ),
]
