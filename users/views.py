from django.shortcuts import render

from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer
from .models import User

# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserInformationView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(pk=request.user.id).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
