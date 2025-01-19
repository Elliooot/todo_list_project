from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
# Create your views here.

# Task List
def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

# Add Task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title') # get title in the list
        Task.objects.create(title=title) # create new task
        return redirect('index')
    
# Delete Task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')

# Toggle Completion Status
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)    
    task.completed = not task.completed
    task.save()
    return redirect('index')