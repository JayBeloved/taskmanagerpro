from django.db.models.base import Model
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Input Classes

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'


catform = CategoryForm()

class TaskForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = '__all__'

tsform = TaskForm()

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

tdform = TodoForm()


# Create your views here.

app_name = "taskmgr"
def index(request):
    return render(request, "taskmgr/index.html", {
        
    })

def dashboard(request):
    return render(request, "taskmgr/dashboard.html", {
        "categories": Categories.objects.all(),
        "tasks": Tasklist.objects.all(),
        "todos": Todo.objects.all(),
        "activetasks": ActiveTasks.objects.all()
    })

def new(request):

    return render(request, "taskmgr/new.html", {
    })

def newcategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            c = CategoryForm(request.POST)
            c.save()
            return HttpResponseRedirect(reverse("taskmgr:dashboard"))
        else:
            return render(request, "taskmgr/newcategory.html", {
                "catform": form
            })
    return render(request, 'taskmgr/newcategory.html', {
        "catform": catform

    })


def newtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            s = TaskForm(request.POST)
            s.save()
            return HttpResponseRedirect(reverse("taskmgr:dashboard"))
        else:
            return render(request, "taskmgr/newtask.html", {
                "tsform": form
            })
    return render(request, 'taskmgr/newtask.html', {
        "tsform": tsform
    })


def newtodo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            d = TodoForm(request.POST)
            d.save()
            return HttpResponseRedirect(reverse("taskmgr:dashboard"))
        else:
            return render(request, "taskmgr/newtodo.html", {
                "tdform": form
            })
    return render(request, 'taskmgr/newtodo.html', {
        "tdform": tdform
    })


def login(request):
    return render(request, "taskmgr/login.html",{

    })

