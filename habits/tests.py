from django.test import TestCase
from .models import Habit, Task
from django.contrib.auth.models import User
import pandas as pd
from datetime import date
        
# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        df_tasks = pd.read_csv('simulated_tasks.csv')

        testuser = User.objects.create_user(username='testuser2', password='h0l4123**')
        
        habits = ['Yoga', 'Run', 'Meditation', 'Read Book', 'Write Diary']
        freq = ['WEEKLY', 'WEEKLY', 'DAILY', 'WEEKLY', 'DAILY']
        
        for i,j in zip(habits,freq):
            habit = Habit.objects.create(habit_title=i, user_id=testuser.id, frequency=j)
            df_task_data = df_tasks[df_tasks.habit_id == i]
            print(df_task_data)

            for c, d in zip(df_task_data.checked, df_task_data.date):
                task = Task(habit_id=habit.id, checked=c, date=d)
                task.save()

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_read_book_streak(self):
        read_book = Habit.objects.get(
            habit_title='Read Book',
        )
        
        self.assertEqual(read_book.streak, 4)

    def test_run_streak(self):
        run = Habit.objects.get(
            habit_title='Run',
        )
        
        self.assertEqual(run.streak, 8)

    def test_yoga_streak(self):
        yoga = Habit.objects.get(
            habit_title='Yoga',
        )
        
        self.assertEqual(yoga.streak, 8)

    def test_meditation_streak(self):
        meditation = Habit.objects.get(
            habit_title='Meditation',
        )
        
        self.assertEqual(meditation.streak, 2)

    def test_write_diary_streak(self):
        write_diary = Habit.objects.get(
            habit_title='Write Diary',
        )
        
        self.assertEqual(write_diary.streak, 4)
        

    def test_longest_daily_streak(self):
        
        longest_streak = Habit.objects.filter(
            frequency = 'DAILY'
        ).latest('streak')
        
        self.assertEqual(longest_streak.habit_title, 'Write Diary')        

    def test_longest_streak(self):
        
        longest_streak = Habit.objects.latest('streak')
        
        self.assertEqual(longest_streak.habit_title, 'Yoga')

    def test_shortest_streak(self):
        
        longest_streak = Habit.objects.earliest('streak')
        
        self.assertEqual(longest_streak.habit_title, 'Meditation')
        
    def test_latest_date(self):
        
        latest_day = Task.objects.latest('date')
        
        self.assertEqual(latest_day.date, date(2021, 12, 12))

    def test_first_date(self):
        
        first_day = Task.objects.earliest('date')
        
        self.assertEqual(first_day.date, date(2021, 10, 18))