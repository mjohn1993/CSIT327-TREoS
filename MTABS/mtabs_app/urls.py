from django.urls import path
from .views import landing_page, login_page, register_page

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Example for landing page
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
]
