from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth import get_user_model
from .models import *
from .serializers import *
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template import Context

import os
import environ
from dotenv import load_dotenv

load_dotenv()

env = environ.Env(
    # set casting, default value
    DEBUUG=(bool, False)
    )


User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = Groups.objects.filter(user1 = user)
            groups = []
            for g in group:
                groups.append(g.id)
            return Response({'message':'Logged In','user':{'id':user.id,'username':user.username},"groups_id":groups},status=status.HTTP_200_OK)
        else:
            return Response({"message":"No User Found"},status=status.HTTP_401_UNAUTHORIZED)

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
        group_id = request.data.get('group_id')
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        if group_id:
            invites = Invitation.objects.get(email = email)
            invites.user_joined = True
            invites.save()


            group = Groups.objects.get(id=group_id)

            if not group.user2:
                group.user2 = user
            elif not group.user3:
                group.user3 = user
            elif not group.user4:
                group.user4 = user

            group.save()


        return Response({'message': 'User is created','user':{'id':user.id,'username':user.username}},status=status.HTTP_201_CREATED)

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

class getGroup(generics.GenericAPIView):
    def get(self,request):
        group_id = request.query_params.get('group_id')
        group = Groups.objects.filter(id = group_id)
        group_serializer = GroupSerializer(group, many=True)
        group_data = group_serializer.data[0]

        invites_querset  = Invitation.objects.filter(group_id = group_id)
        
        
        response = {}
        response['group_id'] = group_data['pk']
        response['group_name'] = group_data['group_name']
        response['user'] = []
        response['user'] .append({"user": group_data['username1'], "user_id":group_data['user1'], "status": "Group Leader"})


        if 'username2' in group_data.keys() :
            response['user'] .append({"user": group_data['username2'], "user_id":group_data['user2'], "status": "Group Member"})
            
        if 'username3' in group_data.keys():
            response['user'] .append({"user": group_data['username3'], "user_id":group_data['user3'],"status": "Group Member"})
        if 'username4' in group_data.keys():
            response['user'] .append({"user": group_data['username4'], "user_id":group_data['user4'],"status": "Group Member"})

        if invites_querset:
            for data in invites_querset:
                if data.user_joined == False:
                    invitee = data.email
                    response['user'] .append({"user": invitee, "status": "Invited"})

        return Response(response)
 

class addUserToGroup(generics.GenericAPIView):

    def post(self,request):
        user_email = request.data.get('user_email')
        user_id = request.data.get("user_id")
        group_id = request.data.get("group_id")
        serializer = InvitationSerializer(data = {"group_id": group_id, "email": user_email})
        if serializer.is_valid():
            user = User.objects.filter(id=user_id)
            group = Groups.objects.filter(id=group_id)
            if not group:
                return Response({"message":"Group Id not valid", "Id":group_id}, status =status.HTTP_404_NOT_FOUND)
            if not user:
                return Response({"message":"Used Id not valid", "Id":user_id}, status = status.HTTP_404_NOT_FOUND)


            username = user[0].first_name +" "+ user[0].last_name
            url =os.environ['FRONT_URL']+"/regitser/"+group_id
            plaintext = get_template('email.txt')
            htmly = get_template('email.html')
            d = { 'username': username, 'my_url': url}
            text_content = plaintext.render(d)
            html_content = htmly.render(d)

            msg = EmailMultiAlternatives("You are Invited!", text_content, "info@challenge4-team58.com", [user_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            serializer.save()

            

            return Response({"message":"Invited Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"Invalid Response", "user_email":user_email, "user_id":user_id, "group_id":group_id}, status = status.HTTP_401_UNAUTHORIZED)

            





        



