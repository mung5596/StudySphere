from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class StudyGroupForm(forms.ModelForm):
    class Meta:
        model = StudyGroup
        fields = [
            "name",
            "subject",
            "venue",
            "date",
            "start_time",
            "end_time",
            "max_people",
            "year_group",
            "description",
        ]
