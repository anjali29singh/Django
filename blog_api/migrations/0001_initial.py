# Generated by Django 5.1.1 on 2025-01-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("created_at", models.DateTimeField()),
                ("title", models.CharField(blank=True, max_length=100)),
                ("content", models.TextField()),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]