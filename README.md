# Habit tracker app

The aim of this project is to create a Habit tracker app built with python. For this work, I used Django as a tool to build this program. 

## Installation of Django 
* This app was built using django. Therefore, Django extension has to be installed. Please to do this just follow the guidelines provided in the following link: 
https://docs.djangoproject.com/en/1.8/howto/windows/

## Running the program

* The Django Model-Template-View (MTV) requires that for each modification in the model you need to run the following command to prepare the migration: 

``python manage.py makemigrations``

* Then, a migration File is created. Then, running the following command will migrates the data:

``python manage.py migrate``

* To run the server, just write the next command:

``python manage.py runserver``

## Creating a user

* This will will open the server in your browser in the view log in / sign up. If you are a new user please click on sign up and create your account. Otherwise, please insert your username and password. Once you create the new user, you will find 5 predefine habits, you can use them or delete them. Enjoy!

## Check habits

* From this point, everything is quite intuitive. The browser will show you the habits view with all the habits you added and the predefined habits. There, you can delete, add or check your habits. In order to check your habits, please press the button check and add the date in the following format:

'yyyy-mm-dd'

* Then please click on the check task button and you will be redirected to the habits table

* The program will calculate automatically the streaks and if you break the habit. 

## Add new habit

* Please click on the button 'new habit' and you will be forwarded to the new habit view where you can introduce a name for your habit and the frequency choice between daily and weekly. Then, please click on submit and you will be redirected to your habits table.

## Delete habits
* Click on the delete button in habits view and it will be immediately removed. 

## Testing

* Please use the csv file as data source. It contains 4 weeks data coverage for the predefine habits.