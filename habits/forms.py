from django import forms
from django.forms import ModelForm
from .models import Habit, Task
from datetime import datetime
from habits.models import *
from django import forms

class HabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = ['habit_title', 'frequency']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['date']