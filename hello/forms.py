from django import forms
from .models import MyModel
from .models import Task

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('field1','field2')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')