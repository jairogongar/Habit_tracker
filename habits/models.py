from django.db import models
from django.conf import settings
from django.http import request
from datetime import timedelta

FREQUENCY_CHOICES = [
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
]

# Create your models here.
class Habit(models.Model):
    """
    This model contains information about the Habit
    
    It may receive as parameters the
    habit_title: str
    frequency: 'DAILY' or 'WEEKLY'
    user: int
    """
    habit_title = models.CharField(max_length=200)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.habit_title

class Task(models.Model):
    """
    This model contains the information for the tasks (i.e., the dates
    when you check in for a habit). The parameters passed may be:
    habit_id: int
    checked: bool
    date: str/datetime object
    """
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    checked = models.BooleanField()
    date = models.DateField()
    

    def save(self, *args, **kwargs):
        """
        This function is an extension of the save method.
        
        The intention is to update the streak for the habit every time
        a new task is checked.
        """
        super().save(*args, **kwargs)
        if self.habit.frequency == 'DAILY':
            tasks = Task.objects.filter(
                habit_id = self.habit.id,
                habit__frequency = self.habit.frequency
            )

            dates = list(set([d.date for d in tasks]))
            dates.sort()

            acum = []
            if len(dates) > 1:
                for i in range(1, len(dates)):
                    if dates[i] == dates[i-1] + timedelta(days=1):
                        if i == 1:
                            acum.append(dates[i-1])
                            acum.append(dates[i])
                        else:
                            acum.append(dates[i])

                    else:
                        acum = [dates[i]]
            else:
                acum = dates
            
            self.habit.streak = len(acum)

            self.habit.save()

        elif self.habit.frequency == 'WEEKLY':

            tasks = Task.objects.filter(
                habit_id = self.habit.id,
                habit__frequency = self.habit.frequency
            )

            dates = list(set([d.date for d in tasks]))
            dates.sort()

            acum = []
            if len(dates) > 1:
                for i in range(1, len(dates)):
                    if dates[i].isocalendar().week - dates[i-1].isocalendar().week == 1:
                        if i == 1:
                            acum.append(dates[i-1])
                            acum.append(dates[i])
                        else:
                            acum.append(dates[i])

                    else:
                        acum = [dates[i]]
            else:
                acum = dates
                        
            self.habit.streak = len(acum)
            self.habit.save()
    
    def __str__(self):
        return f'On day {self.date}, habit {self.habit} was {str(self.checked)}'