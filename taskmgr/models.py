from django.db import models

# Create Choice Classes


class Priority(models.TextChoices):
    URGIMP = ("UI", "Urgent-Important"),
    URGUNIMP = ("UU", "Urgent-Unimportant"),
    NOTURGIMP = ("NI", "NotUrgent-Important"),
    NOTURGUNIMP = ("NU", "NotUrgent-Unimportant")


class Status(models.TextChoices):
    NOTSTARTED = ("NS", "Not_Started"),
    ONGOING = ("OG", 'Ongoing'),
    COMPLETED = ("CP", "Completed")

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    catcode = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.category} with description: {self.description}, code: {self.catcode}"

class Tasklist(models.Model):
    catcode = models.CharField(max_length=5)
    task = models.CharField(max_length=60)
    taskcode = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.catcode} with task: {self.task}, code: {self.taskcode}"


class Todo(models.Model):
    priority = models.CharField(max_length=40, choices=Priority.choices, default=Priority.URGUNIMP)
    taskcode = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.NOTSTARTED)
    activity = models.CharField(max_length=300)
    tdcode = models.CharField(max_length=30)

    def __str__(self):
        return f"Task Priority - {Priority(self.priority).label}; Taskcode - {self.taskcode}; Status - {self.status}; Activity - {self.activity}"
        


class ActiveTasks(models.Model):
    tdcode = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=Status.choices)
    start = models.DateField()
    end = models.DateField(null=True)
    duration = models.DurationField(null=True)

    def __str__(self):
        return f"{self.tdcode} - Status : {Status(self.status).label}, Started on {self.start}"
