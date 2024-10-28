from django.urls import path
from .views import landing_page, login_page, register_page, dashboard_page, calendar_page, reminder_page

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Example for landing page
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('CalendarMonth/', calendar_page, name='calendar_page'),
    path('Reminders/', reminder_page, name='reminder_page'),
]
