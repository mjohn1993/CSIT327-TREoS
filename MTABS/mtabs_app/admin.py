from django.contrib import admin
from .models import Reminder, Task, Event, User

admin.site.register(User)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    fields = ('title', 'completed', 'user')  # Include user field
    search_fields = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'user')  # Include user field
    search_fields = ('event_name',)

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'user')  # Include user field
    fields = ('title', 'time', 'user')  # Include user field in form
    search_fields = ('title',)
