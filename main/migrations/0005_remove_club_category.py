# Generated by Django 4.1.7 on 2023-03-08 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_club_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="club",
            name="category",
        ),
    ]
