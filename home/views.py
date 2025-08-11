from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

def homepage(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('id')
        return render(request, 'home/homepage.html', {'tasks': tasks})  
    return render(request, 'home/homepage.html')



def add_task(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        title = request.POST.get('task')
        print(f"Received task title: {title}")
        if title:
            task = Task(title=title, user=request.user)
            task.save()
    return redirect('homepage')


def complete_task(request, task_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.task_completed = True
            task.save()
        except Task.DoesNotExist:
            return redirect('homepage')
    
    return redirect('homepage')


@login_required
def clear_tasks(request):
    if request.method == 'POST':
        request.user.tasks.all().delete()
    return redirect('homepage')


