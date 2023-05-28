# Generated by Django 4.2 on 2023-05-28 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="gender",
            field=models.CharField(
                choices=[("M", "Man"), ("W", "Women"), ("C", "Common")],
                default="C",
                max_length=10,
            ),
        ),
    ]