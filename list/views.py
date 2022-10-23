import django.views.generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class Task_listview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class Detaail_view(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

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