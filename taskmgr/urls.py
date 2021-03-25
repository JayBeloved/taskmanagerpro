from django.urls import path

from . import views

app_name = "taskmgr"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("new/", views.new, name="new"),
    path("new/category/", views.newcategory, name="newcategory"),
    path("new/task/", views.newtask, name="newtask"),
    path("new/todo/", views.newtodo, name="newtodo"),
]
