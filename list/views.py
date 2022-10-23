import django.views.generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
# Create your views here.

class Task_listview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

def task_view(request):
    obj1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority= request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date= date)
        obj.save()
    return render(request,'task_view.html', {'obj1':obj1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task':task})

def update(request, taskid):
    task = Task.objects.get(id=taskid)
    forms = Todoforms(request.POST or None, instance=task)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request, 'edit.html', {task:task,'forms': forms})