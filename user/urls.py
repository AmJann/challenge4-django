from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('check_user_logged_in/', CheckUserLoggedInView.as_view(), name='check_user_logged_in'),
    path('create-group/', createGroup.as_view(), name='create_group'),
    path('add-user-to-group/', addUserToGroup.as_view(), name='add_user_to_group'),
    path('get-group/', getGroup.as_view(), name = 'Get Group')
]
