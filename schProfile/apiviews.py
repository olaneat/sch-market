from rest_framework import generics
from .serializers import SchoolProfileSerializer
from .models import schoolProfile 
from rest_framework import permissions


class ProfileListView(generics.ListAPIView):
  queryset = schoolProfile.objects.all()
  serializer_class = SchoolProfileSerializer
  permission_class = (permissions.IsAdminUser,)

class CreateProfileView(generics.CreateAPIView):
  queryset = schoolProfile.objects.all()
  serializer_class = SchoolProfileSerializer
  permission_class = [permissions.IsAuthenticated]
  

class SchoolProfileDetailView(generics.RetrieveAPIView):
  queryset = schoolProfile.objects.all()
  serializer_class = SchoolProfileSerializer
  permission_class = [permissions.IsAuthenticated]

class DeleteSchoolProfile(generics.DestroyAPIView):
  queryset = schoolProfile.objects.all()
  serializer_class = SchoolProfileSerializer
  permission_class = [permissions.IsAuthenticated]


class updateSchoolProfile(generics.UpdateAPIView):
  queryset = schoolProfile.objects.all()
  serializer_class = SchoolProfileSerializer
  permission_class = [permissions.IsAuthenticated]