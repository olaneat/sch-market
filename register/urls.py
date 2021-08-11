from django.urls import path, re_path
from . import views
from .apiviews import UserDetail, RegistrationAPIView, LoginAPIView, PasswordTokenAPIView, RequestPasswordResetAPIView, CreatePasswordAPI, ChangePasswordAPI
from . import apiviews

app_name = 'register'
urlpatterns = [
    path('registration', RegistrationAPIView.as_view(), name='register'),
    path('<int:pk>/user-detail', UserDetail.as_view(), name='user_detail'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('password-reset/<uidb64>/<token>',
         PasswordTokenAPIView.as_view(), name='password-reset-confirmed'),
    path('request-password', RequestPasswordResetAPIView.as_view(),
         name='request-password'),
    path('password-reset-successful',
         CreatePasswordAPI.as_view(), name='password_changed'),
    path('<int:pk>/change-password',
         ChangePasswordAPI.as_view(), name="change-password")

]


'''path('reset_password', include('django_rest_passwordreset.urls', namespace='password_reset')),
                path('reset_password/confirm', include('django_rest_passwordreset.urls', namespace='password_reset'))'''
