from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    fields = ('title', 'completed')
    search_fields = ('title',)
