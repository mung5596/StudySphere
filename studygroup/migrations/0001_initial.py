# Generated by Django 5.1.6 on 2025-03-03 06:36

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StudyGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=100)),
                ("venue", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "max_people",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(2)]
                    ),
                ),
                ("current_people", models.IntegerField(default=1)),
                (
                    "year_group",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(13),
                            django.core.validators.MinValueValidator(7),
                        ]
                    ),
                ),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OP", "Open"),
                            ("CO", "Completed"),
                            ("CA", "Cancelled"),
                        ],
                        default="OP",
                        max_length=2,
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "participants",
                    models.ManyToManyField(
                        blank=True,
                        related_name="joined_studygroups",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
