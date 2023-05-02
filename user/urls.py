from django.urls import path
from .views import LoginView, LogoutView, RegistrationView, CheckUserLoggedInView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('check_user_logged_in/', CheckUserLoggedInView.as_view(), name='check_user_logged_in'),
]
