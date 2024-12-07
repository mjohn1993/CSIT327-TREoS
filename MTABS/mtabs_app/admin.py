from django.contrib import admin
from .models import Reminder, Task
from .models import Event
from .models import User

admin.site.register(User)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    fields = ('title', 'completed')
    search_fields = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date')  # Changed 'event_date' to 'date'
    search_fields = ('event_name',)  # Enable search by event name

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')  # Display title and time in the list view
    fields = ('title', 'time')  # Fields displayed in the admin form
    search_fields = ('title',)  # Enable search by title