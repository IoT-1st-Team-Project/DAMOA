# Generated by Django 4.1.7 on 2023-03-15 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_reply_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="board",
            name="author",
        ),
        migrations.RemoveField(
            model_name="reply",
            name="author",
        ),
    ]