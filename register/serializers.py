from django.db.models import fields
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import update_last_login
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.utils.encoding import smart_str, force_str, DjangoUnicodeDecodeError, smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login
from schProfile.models import Profile
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from schProfile.serializers import schoolProfileSerializer
from schProfile.models import Profile
from .models import CustomUser
from rest_framework import serializers


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                ' email & password not found.'
            )

        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except user.DoesNotExist:
            raise serializers.ValidationError(
                'user found'
            )

        return {
            'email': user.email,
            'id': user.id,
            'token': jwt_token
        }
        '''if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
            if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
        }
        '''


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )

   # token = serializers.CharField(max_length=255, read_only=True)
    profile = schoolProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'profile')

    def create(self, validated_data):
        return CustomUser.objects._create_user(**validated_data)

    '''
    def create(request, *args, **kwargs):
        user = CustomUser.objects.create(
            email=request['email'],
            password=request['password']
        )
        user.set_password(request['password'])
        user.save()
        return user
    
    
           '''


class RequestNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=250)

    class Meta:
        fields = ['email']


class CreatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=1, max_length=50, write_only=True)
    token = serializers.CharField(
        min_length=1, max_length=50, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, max_length=250, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise Exception()

            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)
