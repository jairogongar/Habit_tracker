from django.contrib import admin

# Register your models here.
from .models import Habit, Task

admin.site.register([Task,Habit])