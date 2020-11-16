from django.shortcuts import get_object_or_404, redirect, render
from allauth.account.views import  LogoutView 
from allauth.account.views import SignupView as BaseSignupView
from django.views.generic import TemplateView
from .models import CustomUser

