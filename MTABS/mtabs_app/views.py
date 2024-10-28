from django.shortcuts import render
from django.http import HttpResponse

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
