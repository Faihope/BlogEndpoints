# Generated by Django 4.0.5 on 2022-06-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0002_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]