from django.urls import path

from . import views

urlpatterns = [
    path('user_habits', views.habits_view, name='habits_view'),
    path('user_habits/<int:habit_id>', views.task_view, name='task_view'),
    path('new_habit', views.new_habit_view, name='new_habit'),
    path('delete_record', views.delete_record, name='delete_record'),
]