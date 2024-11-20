from django import forms
from .models import Task,Event

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']