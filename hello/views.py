from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import MyForm

def hello(request):
    return HttpResponse('Hello World')
def list(request):
    return HttpResponse('Hello list')
def inputformfunction(request):
    form = MyForm()
    return render(request,'my_template.html',{'form':form})