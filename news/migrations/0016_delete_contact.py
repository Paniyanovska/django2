# Generated by Django 4.1.2 on 2022-12-07 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0015_contact"),
    ]

    operations = [
        migrations.DeleteModel(name="Contact",),
    ]
