# Generated by Django 4.1.7 on 2023-03-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_auto_20230313_1250"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]