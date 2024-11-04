from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Task
import json
from .forms import TaskForm
from django.views.decorators.http import require_POST


def landing_page(request):
    return render(request, 'landing.html')

def login_page(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        # Authentication logic goes here
        return HttpResponse(f'Logged in as: {user_id}')
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html') 

def dashboard_page(request):
    return render(request, 'dashboard.html')

def calendar_page(request):
    return render(request, 'CalendarMonth.html')

def reminder_page(request):
    return render(request, 'Reminders.html')

def settings_page(request):
    return render(request, 'Settings.html')

def statistics_page(request):
    return render(request, 'Statistics.html')

def get_tasks(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values('id', 'title', 'completed'))  # Fetch all tasks
        return JsonResponse({'tasks': tasks})

@csrf_exempt  # Remove this if you're using CSRF protection properly
def create_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')

            # Create a new task
            task = Task.objects.create(title=title)
            return JsonResponse({'success': True, 'task': {'id': task.id, 'title': task.title, 'completed': task.completed}})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        data = json.loads(request.body)
        task.title = data['title']
        task.save()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_http_methods(["DELETE"])
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Task not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@require_POST
def complete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed  # Toggle completion status
        task.save()
        return JsonResponse({'success': True, 'completed': task.completed})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found.'})