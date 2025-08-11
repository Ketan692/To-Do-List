from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_task/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('clear_tasks/', views.clear_tasks, name='clear_tasks'),

]
