from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context ={'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
        
    return render(request, 'task/index.html', context)

def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {"form": form}
    return render(request, 'task/update.html', context)


def DeleteTask(request, pk):

    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    return render(request, 'task/delete.html', context)