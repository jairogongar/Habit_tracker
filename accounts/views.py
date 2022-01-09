from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render
from django.contrib.auth import login, authenticate

from habits.models import Habit
from .forms import SignUpForm
from django.shortcuts import render, redirect

def home_view(request):
    """
    The function receives the request from the url and renders the template `home.html`
    """
    
    return render(request, 'home.html')

def signup_view(request):
    """
    The function receives a request from the url and creates a form with `html` to
    create a new user.
    
    If the user introduced the information correctly, they will be signed up and
    returned to `home view`.
    
    Otherwise, they would be taken to the same form to introduce the data correctly,
    returning to the `signup template`
    """
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)

        print(user.id)

        p = Habit(
            habit_title = 'Yoga',
            frequency = 'WEEKLY',
            user_id = user.id
        )
        
        print(p)
        print(p.__dict__)
        p.save()
        print(p)
        print(p.__dict__)

        p = Habit(
            habit_title = 'Run',
            frequency = 'WEEKLY',
            user_id = user.id
        )

        p.save()

        p = Habit(
            habit_title = 'Meditation',
            frequency = 'DAILY',
            user_id = user.id
        )

        p.save()

        p = Habit(
            habit_title = 'Read Book',
            frequency = 'WEEKLY',
            user_id = user.id
        )

        p.save()

        p = Habit(
            habit_title = 'Write Diary',
            frequency = 'DAILY',
            user_id = user.id
        )

        p.save()

        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})