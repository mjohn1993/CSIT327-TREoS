from django.urls import path
from .views import landing_page, login_page, register_page, dashboard_page

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Example for landing page
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_page, name='dashboard_page'),
]
