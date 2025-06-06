from django.db import models

from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id


class Calendar(models.Model):
    calendar_id = models.CharField(max_length=15, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.calendar_id


class Schedule(models.Model):
    schedule_id = models.CharField(max_length=15, primary_key=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    #wowwwwww
    #I'm here


class Event(models.Model):
    event_id = models.CharField(max_length=15, primary_key=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.event_name


class ToDoList(models.Model):
    to_do_list_id = models.CharField(max_length=15, primary_key=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return self.title


class Reminder(models.Model):
    reminder_id = models.CharField(max_length=15, primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, null=True, blank=True)
    time = models.TimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

