# Generated by Django 4.2 on 2023-04-10 14:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="firebase_uid",
        ),
    ]
