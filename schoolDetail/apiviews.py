from rest_framework import generics
from .serializers import GallerySerializer, AdmissionSerializer, VideoSerializer
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.parsers import FileUploadParser
from .models import Gallery, Admission, SchoolVideo
from rest_framework import permissions

class GalleryApi(generics.CreateAPIView):
  serializer_class = GallerySerializer
  queryset = Gallery.objects.all()
  permission_classes = [permissions.IsAuthenticated]
  parser_classes = (FileUploadParser)

  def post(self, request, *args, **kwargs):
    file_serializer = GallerySerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DisplayGalleryApi(generics.ListAPIView):
  serializer_class = GallerySerializer
  queryset = Gallery.objects.all()
  permission_classes = (permissions.AllowAny,)


class CreateAdmissionLetter(generics.ListAPIView):
  serializer_class = AdmissionSerializer
  queryset = Admission.objects.all()
  permissions_classes = (permissions.IsAuthenticated)
  parser_classes = (FileUploadParser)

  def post(self, request, *args, **kwargs):
    file = AdmissionSerializer(data=request.data)
    if file.is_valid():
      file.save()
      return Response(file.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file.errors, status=status.HTTP_400_BAD_REQUEST)

class DisplayAdmissionLetter(generics.ListAPIView):
  serializer_class = AdmissionSerializer
  queryset = Admission.objects.all()
  permission_classes = [permissions.AllowAny]


class SchoolVideoAPi(generics.CreateAPIView):
  serializer_class = VideoSerializer
  queryset = SchoolVideo.objects.all()
  permission_class=[permissions.IsAuthenticated]
  parser_classes = (FileUploadParser)

  def post(self, request, *args, **kwargs):
    video = VideoSerializer(data=request.data)
    if video.is_valid():
      video.save()
      return Response(video.data, status=status.HTTP_201_CREATED)
    else:
      return Response(video.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DisplayVideo(generics.ListAPIView):
  serializer_class = VideoSerializer
  queryset = SchoolVideo.objects.all()
  permission_classes = [permissions.AllowAny]