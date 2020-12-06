from rest_framework import generics
from .models import schoolProfile
from rest_framework import permissions
from .serializers import schoolProfileSerializer

class CreateProfileView(generics.CreateAPIView):
  serializer_class = schoolProfileSerializer
  queryset = schoolProfile.objects.all()
  permission_classes = [permissions.AllowAny]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class DisplaySchoolList(generics.ListAPIView):
  serializer_class = schoolProfileSerializer
  queryset = schoolProfile.objects.all()
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DispaySchoolDetail(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  serializer_class = schoolProfileSerializer
  queryset = schoolProfile.objects.all()

class UpdateSchoolProrfile(generics.UpdateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = schoolProfile.objects.all()
  serializer_class = schoolProfileSerializer

class DeleteSchoolProfile(generics.DestroyAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = schoolProfileSerializer
  queryset = schoolProfile.objects.all()
  
