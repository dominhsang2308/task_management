from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('task/', views.task_list , name='task_list'),
    path('complete/', views.complete_task, name='complete_task'),
    path('toggle_complete/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
]