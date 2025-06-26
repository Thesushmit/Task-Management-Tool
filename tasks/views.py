from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'tasks/task_form.html', {'form': form})
