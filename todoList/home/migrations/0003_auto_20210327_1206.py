# Generated by Django 3.1.6 on 2021-03-27 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_task_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='time',
            new_name='TaskTime',
        ),
    ]
