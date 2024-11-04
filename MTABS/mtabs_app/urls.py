from django.urls import path
from .views import landing_page, login_page, register_page, dashboard_page, calendar_page,get_tasks, reminder_page, settings_page,statistics_page,create_task,edit_task, delete_task, complete_task


urlpatterns = [
    path('', landing_page, name='landing_page'),  # Example for landing page
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('CalendarMonth/', calendar_page, name='calendar_page'),
    path('Reminders/', reminder_page, name='reminder_page'),
    path('Settings/', settings_page, name='settings_page'),
    path('Statistics/', statistics_page, name='statistics_page'),
    path('get-tasks/', get_tasks, name='get_tasks'),
    path('create-task/', create_task, name='create_task'),  # Ensure this line is correct
    path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('complete-task/<int:task_id>/', complete_task, name='complete_task'),

]
