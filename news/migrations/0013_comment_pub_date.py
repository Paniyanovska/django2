# Generated by Django 4.1.2 on 2022-11-19 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0012_alter_comment_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
