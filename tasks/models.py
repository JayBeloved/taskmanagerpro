from django.db import models



#Definitions

class Priority(models.TextChoices):
    URGIMP = ("UI", "Urgent-Important"),
    URGUNIMP = ("UU", "Urgent-Unimportant"),
    NOTURGIMP = ("NI", "NotUrgent-Important"),
    NOTURGUNIMP = ("NU", "NotUrgent-Unimportant")

class Status(models.TextChoices):
    NOTSTARTED = ("NS", "Not-Started"),
    ONGOING = ("OG", 'Ongoing'),
    COMPLETED = ("CP", "Completed")


# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=40, default="Enter Category Name")
    description = models.CharField(max_length=300, default="Enter Category Description")
    catcode = models.CharField(max_length=5, default=100)


class TaskList(models.Model):
    #catcode = models.ForeignKey(Categories, on_delete=models.CASCADE, db_column="catcode",related_name="taskcategory")
    task = models.CharField(max_length=60, default="Enter A Task Definition")
    taskcode = models.CharField(max_length=30, default=100)

class Todo(models.Model):
    priority = models.CharField(max_length=40,choices = Priority.choices, default=Priority.URGUNIMP)
    #taskcode = models.ForeignKey(TaskList, on_delete=models.CASCADE, db_column="taskcode",related_name="todos")
    status = models.CharField(max_length=30, choices = Status.choices, default= Status.NOTSTARTED)
    activity = models.CharField(max_length=300, default="Enter Specific Activity related to the task")
    todocode = models.CharField(max_length=30, default=100)

class ActiveTasks(models.Model):
    status = models.CharField(max_length=30, choices=Status.choices)
    start = models.DateField()
    end = models.DateField()
    duration = models.DurationField()

    



