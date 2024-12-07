from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Reminder, Task
import json
from .forms import TaskForm
from django.views.decorators.http import require_POST
from .models import Event
from .models import User
from django.contrib.auth import logout
from django.contrib import messages

def landing_page(request):
    return render(request, 'landing.html')

def login_page(request):
    # Check if user is already logged in
    if 'username' in request.session:
        return redirect('dashboard_page')  # Redirect if user is already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['username'] = user.username
                return redirect('dashboard_page')  # Redirect to dashboard
            else:
                messages.error(request, 'Incorrect password')
                return render(request, 'login.html')  # Show error
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist')
            return render(request, 'login.html')  # Show error

    return render(request, 'login.html')  # For GET request, render login page

def logout_view(request):
    logout(request)  # Logs out the user and clears the session
    return redirect('login_page')  # Redirects to the login page


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Basic validation
        if not username or not password:
            messages.error(request, 'Please fill in all fields.')
            return render(request, 'register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'register.html')

        # Create a new user
        new_user = User(username=username, password=password)
        new_user.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login_page')  # Redirect to the login page after successful registration

    return render(request, 'register.html')

def dashboard_page(request):
    if 'username' not in request.session:
        return redirect('login_page')

    username = request.session.get('username')
    user = User.objects.get(username=username)
    
    return render(request, 'dashboard.html', {'user': user})

def calendar_page(request):
    return render(request, 'CalendarMonth.html')

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
    
def event_list(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'event_list.html', {'events': events})


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            event_name = data.get('title')
            event_location = data.get('location')
            event_date = data.get('date')  # Expecting 'YYYY-MM-DD'

            # Create and save the event without specifying event_id
            event = Event.objects.create(
                event_name=event_name,
                location=event_location,
                date=event_date
            )
            return JsonResponse({'success': True, 'event_id': event.event_id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

@csrf_exempt
def get_events(request):
    if request.method == 'GET':
        events = Event.objects.all().values('event_id', 'event_name', 'location', 'date')
        event_list = list(events)  # Convert QuerySet to list
        return JsonResponse({'events': event_list})
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})

@csrf_exempt
def update_event(request, event_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            event = Event.objects.get(event_id=event_id)
            event.event_name = data.get('title', event.event_name)
            event.location = data.get('location', event.location)
            event.date = data.get('date', event.date)  # Assuming date is also updated
            event.save()
            return JsonResponse({'success': True})
        except Event.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Event not found.'})

@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        try:
            event = Event.objects.get(event_id=event_id)
            event.delete()
            return JsonResponse({'success': True})
        except Event.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Event not found.'})

def update_page(request):
    if request.method == 'POST':
        username = request.session.get('username')
        if username:
            user = User.objects.get(username=username)
            new_username = request.POST.get('new_username')
            new_password = request.POST.get('new_password')

            if new_username:
                request.session['username'] = new_username  # Update session
                user.username = new_username
            if new_password:
                user.password = new_password
            user.save()
            return redirect('dashboard_page')
        else:
            return redirect('login_page')
    
    return render(request, 'update_page.html')

def delete_account(request):
    if request.method == 'POST':
        username = request.session.get('username')
        if username:
            User.objects.filter(username=username).delete()
            request.session.flush()  # Clear the session after deleting the account
            return redirect('login_page')
        else:
            return redirect('login_page')
    
    return render(request, 'delete_page.html')

# Reminder page view
def reminder_page(request):
    return render(request, 'reminders.html')

# Create reminder
@csrf_exempt
def create_reminder(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get('title')
        time = data.get('time')
        if title and time:
            new_reminder = Reminder.objects.create(title=title, time=time)
            return JsonResponse({"id": new_reminder.id, "status": "success"})
        return JsonResponse({"error": "Invalid data"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=405)

# Fetch reminders
def get_reminders(request):
    reminders = Reminder.objects.all().order_by('time')
    data = {"reminders": list(reminders.values('id', 'title', 'time'))}
    return JsonResponse(data)

# Edit reminder
@csrf_exempt
def edit_reminder(request, id):
    if request.method == "PUT":
        try:
            reminder = Reminder.objects.get(id=id)
            data = json.loads(request.body)
            title = data.get('title')
            time = data.get('time')
            if title and time:
                reminder.title = title
                reminder.time = time
                reminder.save()
                return JsonResponse({"status": "success"})
            return JsonResponse({"error": "Invalid data"}, status=400)
        except Reminder.DoesNotExist:
            return JsonResponse({"error": "Reminder not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=405)

# Delete reminder
@csrf_exempt
def delete_reminder(request, id):
    if request.method == "DELETE":
        try:
            reminder = Reminder.objects.get(id=id)
            reminder.delete()
            return JsonResponse({"status": "success"})
        except Reminder.DoesNotExist:
            return JsonResponse({"error": "Reminder not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=405)
