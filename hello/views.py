from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import MyForm
from .models import Task
from .forms import TaskForm

def hello(request):
    return HttpResponse('Hello World')
def list(request):
    return HttpResponse('Hello list')
def inputformfunction(request):
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'my_template.html',{'data':form.cleaned_data})
    else:
        form = MyForm()
        # field1 = form.cleaned_data['field1']
        # field2 = form.cleaned_data['field2']
    
    return render(request,'my_template.html',{'form':form})

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    context = {'tasks':tasks, 'form':form}
    return render(request,'task_list.html',context)


