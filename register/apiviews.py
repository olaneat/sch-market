from rest_framework.response import Response
import json
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        new_user = authenticate(email=request.POST.get('email'),
                                password=request.POST.get('password')
                                )
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                print('login successful')
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'username': serializer.data.get('username', None),
                'email': serializer.data.get('email', None),

            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response = {
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message': 'login successful',
                    'token':  serializer.data['token'],
                    'id': self.request.user.id
                }
                status_code = status.HTTP_200_OK
                return Response(response, status=status_code)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
