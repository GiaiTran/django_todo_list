from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task

# Create your views here.
# def taskList(request):
#     return HttpResponse("Base")

class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    # template_name = 'base/'

class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task