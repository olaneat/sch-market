from rest_framework.response import Response
import json
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import RegistrationSerializer, LoginSerializer
from register.models import CustomUser
from . import permissions


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {

                'username': serializer.data.get('username', None),
                'email': serializer.data.get('email', None)
            },
            status=status.HTTP_201_CREATED,
        )


class CreateProfileView(generics.CreateAPIView):
    parser_classes = (MultiPartParser,)
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
