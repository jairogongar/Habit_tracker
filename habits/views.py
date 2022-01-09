from django.http import HttpResponseRedirect
from django.http.response import HttpResponse

from .forms import HabitForm, TaskForm
from .models import Habit, Task

from django.conf import settings

from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

# Create your views here.
def new_habit_view(request):
	'''
	The function receives a request from the url and creates a form to 
	create a new habit through the `HabitForm()` class defined in `forms.py`.

	Returns the `habit.html` template with the context containing the form.
	'''

	request.session['type'] = 'habit'

	context = {}
	
	form = HabitForm(request.FILES)
	context['form'] = form

	return render(request, 'habit.html', context)


def task_view(request, habit_id):
	'''
	The function receives a request from the url and creates an html form
	for the user to introduce the date in which they completed a task for
	a specific routine, given by the parameter `habit_id`.

	Returns the template `task.html` with the form to input data
	'''
	
	request.session['id'] = habit_id

	request.session['type'] = 'task'

	context = {}
	current_user = request.user

	form = TaskForm(initial={'date': datetime.today().date})

	context['form'] = form

	return render(request, "task.html", context)


def habits_view(request):
	"""
	The function receives a request from the url and apply 2 different functionalities
	if the request is a `POST method`

	1. If request comes with `task` in the instance `session`, the function will introduce
	the completed task on the database and it will also recalculate the `streak` for the
	habit id. It will know how to recalculate the streak for `daily` and `weekly` frequencies.

	2. If request comes with `habit` in the instance `session`, the function will indtroduce
	a new habit for the user.

	In any case, the function will return the `home.html` template where we can observe all
	the habits created untill the moment and their information (streak, frequency)
	"""
    
	context = {}

	if request.method=='POST':
		if request.session.get('type') == 'task':

			id = request.session.get('id')

			form = TaskForm(request.POST)

			if form.is_valid():
				task = form.save(commit=False)
				task.checked = 1
				task.habit_id = id # Variable I take from the id
				task.save()

		else:

			form = HabitForm(request.POST)
			
			if form.is_valid():
				
				habit = form.save(commit=False)
				habit.habit_title = form.cleaned_data['habit_title']
				habit.frequency = form.cleaned_data['frequency']
				habit.user_id = request.user.id

				habit.save()
				
	# Here starts the get method to filter
	current_user = request.user
	user_habits = Habit.objects.filter(user_id = current_user.id)

	context['user_habits'] = user_habits
	daily_habits = user_habits.filter(frequency = 'DAILY')

	if len(user_habits) > 0:
		longest = user_habits.order_by('-streak')[0]
		context['habit_longest_streak'] = longest
		
	context['daily_habits'] = daily_habits

	return render(request, "home.html", context)

def delete_record(request):
	"""
	The function receives a request from the url and deletes the habit where
	the delete button was placed on `home.html` template.
 
	Returns the `habits_view` previously defined, which renders the `home.html`
	template.
	"""

	if request.method == 'POST':
		items_to_delete = request.POST.getlist('delete_items')
		Habit.objects.filter(pk__in=items_to_delete).delete()

	return redirect('habits_view')