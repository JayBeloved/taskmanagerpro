from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse





# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
    })
       
    

def new(request):
    return render(request, "tasks/new.html", {
    })
