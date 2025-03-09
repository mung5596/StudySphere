from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class StudyGroup(models.Model):
    # Django's ORM automatically assigns unique id to instantiations.
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_people = models.IntegerField(validators=[MinValueValidator(2)])
    current_people = models.IntegerField(default=1)
    year_group = models.IntegerField(validators=[MaxValueValidator(13), MinValueValidator(7)])
    description = models.TextField(blank=True)
    participants = models.ManyToManyField(User, related_name="joined_studygroups", blank=True)
    status_choices = [("OP", "Open"), ("CO", "Completed"), ("CA", "Cancelled")]
    status = models.CharField(max_length=2, choices=status_choices, default="OP")

    def __str__(self):
        return self.name