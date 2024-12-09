from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    create_reminder,
    delete_reminder,
    edit_reminder,
    landing_page,
    login_page,
    get_reminders,
    register_page,
    dashboard_page,
    calendar_page,
    get_tasks,
    reminder_page,
    settings_page,
    statistics_page,
    create_task,
    edit_task,
    delete_task,
    complete_task,
    event_list,
    create_event,
    update_event,
    delete_event,
    get_events,
    update_page,
    delete_account,
    logout_view,
)

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
    path('events/', event_list, name='event_list'),
    path('create-event/', create_event, name='create_event'),
    path('update-event/<str:event_id>/', update_event, name='update_event'),
    path('delete-event/<str:event_id>/', delete_event, name='delete_event'),
    path('get-events/', get_events, name='get_events'),  # Add this line
    path('update/', update_page, name='update_page'),
    path('delete/', delete_account, name='delete_account'),
    path('logout/', logout_view, name='logout_page'),
    path('reminders/create/', create_reminder, name='create_reminder'),
    path('reminders/get/', get_reminders, name='get_reminders'),
    path('reminders/edit/<int:id>/', edit_reminder, name='edit_reminder'),
    path('reminders/delete/<int:id>/', delete_reminder, name='delete_reminder'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
