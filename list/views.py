import django.views.generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Task_listview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class Detaail_view(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class Task_update(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs= {'pk':self.object.id})

class Task_delete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


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