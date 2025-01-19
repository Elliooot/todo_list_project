from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Task list page
    path('add/', views.add_task, name='add_task'), #create task page
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), #delete task
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'), #toggle completion status
]