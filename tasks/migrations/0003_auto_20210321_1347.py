# Generated by Django 3.1.7 on 2021-03-21 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20210320_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activetasks',
            name='todocode',
        ),
        migrations.RemoveField(
            model_name='tasklist',
            name='catcode',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='taskcode',
        ),
    ]