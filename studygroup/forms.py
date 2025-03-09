from django import forms
from .models import StudyGroup


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
