from django.contrib import admin
from .models import Task
from .models import Event

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    fields = ('title', 'completed')
    search_fields = ('title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date')  # Changed 'event_date' to 'date'
    search_fields = ('event_name',)  # Enable search by event name