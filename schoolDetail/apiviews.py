from django.db.models import query
from rest_framework import generics
from .serializers import GallerySerializer, AdmissionFormSerializer, VideoSerializer, ReviewSerializer, PricipalDetailSerialiazer, EnquirySerialiazer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from .models import Gallery, Admission, SchoolVideo, Enquiry, PrincipalDetails, Review
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


class CreateAdmissionForm(generics.CreateAPIView):
    serializer_class = AdmissionFormSerializer
    queryset = Admission.objects.all()
    permissions_classes = (permissions.IsAuthenticated)
    parser_classes = (FileUploadParser)

    def post(self, request, *args, **kwargs):
        file = AdmissionFormSerializer(data=request.data)
        if file.is_valid():
            file.save()
            return Response(file.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveAdmissionForm(generics.RetrieveAPIView):
    serializer_class = AdmissionFormSerializer

    def get_queryset(self):
        queryset = Admission.objects.filter(
            id=self.request.GET.get('admission.id'))
        return queryset


class SchoolVideoAPi(generics.CreateAPIView):
    serializer_class = VideoSerializer
    queryset = SchoolVideo.objects.all()
    permission_class = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.school_video
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            message='Video successfully Uploaded',
            status=status.HTTPS_201_CREATED,
            headers=headers,
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile.school_video)

    '''
    
         def post(self, request, *args, **kwargs):
        video = VideoSerializer(data=request.data)
        if video.is_valid():
            video.save()
            return Response(video.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video.errors, status=status.HTTP_400_BAD_REQUEST)
    '''


class DisplayVideo(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = SchoolVideo.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = VideoSerializer.objects.filter(
            id=self.request.GET.get('user.id'))
        return queryset


class CreatePrincipalDetailView(generics.CreateAPIView):
    serializer_class = PricipalDetailSerialiazer
    parser_classes = (MultiPartParser, FormParser)
    queryset = PrincipalDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.principal_detail
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            message='Principal Data Successfully save',
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)


class DisplayPrincipalDetialView(generics.RetrieveAPIView):
    serializer_class = PrincipalDetails
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_querryset(self):
        queryset = PrincipalDetails.objects.filter(
            id=self.request.GET.get('user.id'))
        return queryset
