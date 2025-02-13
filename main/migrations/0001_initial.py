# Generated by Django 5.1.1 on 2024-10-10 15:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Errors",
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
                ("name", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=15)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="FreeDate",
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
                ("date", models.DateField(unique=True)),
                ("free", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("price", models.CharField(max_length=10, null=True)),
                (
                    "durations",
                    models.DurationField(default=datetime.timedelta(seconds=3600)),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notes",
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
                ("name", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=15)),
                ("date", models.DateField(blank=True)),
                ("time", models.CharField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.service"
                    ),
                ),
            ],
        ),
    ]
