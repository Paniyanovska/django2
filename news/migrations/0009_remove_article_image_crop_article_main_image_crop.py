# Generated by Django 4.1.2 on 2022-11-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0008_article_image_crop"),
    ]

    operations = [
        migrations.RemoveField(model_name="article", name="image_crop",),
        migrations.AddField(
            model_name="article",
            name="main_image_crop",
            field=models.ImageField(default=0, upload_to="images"),
            preserve_default=False,
        ),
    ]