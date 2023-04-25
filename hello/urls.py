from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello),
    path('list',views.list),
    path('inputform',views.inputformfunction),
    path('', views.task_list, name='task_list'),
]