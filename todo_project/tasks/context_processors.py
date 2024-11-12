from .models import Task

def task_count_processor(request):
    task_count = Task.objects.count()
    return {
        'task_count' : task_count
    }