# Generated by Django 4.2 on 2023-05-30 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0003_purchase_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="size",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
