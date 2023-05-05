from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
from django.http import JsonResponse

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            res ={'username':username}
            return JsonResponse(res)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class RegistrationView(APIView):
    def post(self, request):
        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        return Response({'message': 'User is created'},status=status.HTTP_201_CREATED)

class CheckUserLoggedInView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class createGroup(generics.CreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer

class addUserToGroup(generics.GenericAPIView):
    serializer_class = GroupSerializer

    def post(self,request):
        user_id = request.data.get('user_id')
        group_id = request.data.get('group_id')
        
        group = Groups.objects.get(id=group_id)
        user = User.objects.get(id = int(user_id))
        position = ''

        if not group.user2:
            group.user2 = user
            position = 'user2'
        elif not group.user3:
            group.user3 = user
            position = 'user3'
        elif not group.user4:
            group.user4 = user
            position = 'user4'

        else:
            return Response({'error': 'No position available in group.'}, status=status.HTTP_400_BAD_REQUEST)

        group.save()

        serializer = GroupSerializer(group)
        return Response({'position': position, 'group': serializer.data})


