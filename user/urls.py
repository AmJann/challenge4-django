from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('check_user_logged_in/', CheckUserLoggedInView.as_view(), name='check_user_logged_in'),
    path('create_group/', createGroup.as_view(), name='create_group'),
    path('add_user_to_group/', addUserToGroup.as_view(), name='add_user_to_group')
]
