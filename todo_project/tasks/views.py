from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def task_list(request):
    

    tasks = Task.objects.all()
    task_count = tasks.count()
    return render(request, 'task_list.html',{'tasks': tasks},{'task_count': task_count})

def complete_task(request):
    completed_task = Task.objects.filter(completed=True)
    return render(request, 'complete_task.html', {'tasks' : completed_task})