# Generated by Django 4.0.5 on 2022-06-21 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
