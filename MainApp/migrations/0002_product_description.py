# Generated by Django 4.1.5 on 2023-01-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
