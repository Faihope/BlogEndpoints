# Generated by Django 4.0.5 on 2022-06-26 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
    ]
