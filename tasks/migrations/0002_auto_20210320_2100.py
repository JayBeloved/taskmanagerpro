# Generated by Django 3.1.7 on 2021-03-20 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activetasks',
            name='todocode',
            field=models.ForeignKey(db_column='todocode', on_delete=django.db.models.deletion.CASCADE, related_name='activetasks', to='tasks.todo'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='catcode',
            field=models.ForeignKey(db_column='catcode', on_delete=django.db.models.deletion.CASCADE, related_name='taskcategory', to='tasks.categories'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='taskcode',
            field=models.ForeignKey(db_column='taskcode', on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='tasks.tasklist'),
        ),
    ]
