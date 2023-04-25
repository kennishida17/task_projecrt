from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World')
def list(request):
    return HttpResponse('Hello list')