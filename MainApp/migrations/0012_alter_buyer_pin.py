# Generated by Django 4.1.5 on 2023-02-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0011_rename_pincode_buyer_pin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyer",
            name="pin",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
