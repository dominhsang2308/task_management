from django.utils import timezone
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Task
# Create your views here.

def dashboard(request):
    return render(request,'base.html')

def task_list(request):
    

    tasks = Task.objects.all()
    task_count = tasks.count()
    return render(request, 'task_list.html',{'tasks': tasks},{'task_count': task_count})

def complete_task(request):
    completed_task = Task.objects.filter(completed=True)
    return render(request, 'complete_task.html', {'tasks' : completed_task})

def task_list(request):
    if request.method == 'POST':
        # Lấy tiêu đề task từ form
        task_title = request.POST.get('task_title')
        # Nếu tiêu đề không rỗng, tạo một task mới
        if task_title:
            Task.objects.create(title=task_title,due_date=timezone.now().date())
        # Redirect về trang task_list sau khi thêm task để tránh việc gửi lại dữ liệu khi người dùng refresh
        return redirect('task_list')

    # Lấy tất cả các task để hiển thị trong trang
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, task_id)
    task.completed = not Task.completed
    task.save()
    return redirect('task_list')
