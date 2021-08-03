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
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        profile = self.request.user.profile
        queryset = Gallery.objects.filter(user=profile)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.gallery.first()
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = {
            'message': 'Pictures successfully Uploaded',
            'status': status.HTTP_201_CREATED,
            'headers': headers,
            'serializer': serializer.data
        }
        return Response(res)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile)


class DisplayGalleryApi(generics.ListAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
    permission_classes = (permissions.AllowAny,)


class CreateAdmissionForm(generics.CreateAPIView):
    serializer_class = AdmissionFormSerializer
    queryset = Admission.objects.all()
    permissions_classes = (permissions.IsAuthenticated)
    parser_classes = (FileUploadParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.admission_form.filter(
                id=self.request.user.id)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(data=request.data)
        response = {
            'message': 'Gallery successfully Created',
            'status': status.HTTP_201_CREATED,
            'headers': headers,
            'success': True
        }

        return Response(response)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile)
    '''

         def post(self, request, *args, **kwargs):
        file = AdmissionFormSerializer(data=request.data)
        if file.is_valid():
            file.save()
            return Response(file.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file.errors, status=status.HTTP_400_BAD_REQUEST)
    
    '''


class RetrieveAdmissionForm(generics.RetrieveAPIView):
    serializer_class = AdmissionFormSerializer

    def get_queryset(self):
        queryset = Admission.objects.filter(
            id=self.request.GET.get('admission.id'))
        return queryset


class SchoolVideoAPi(generics.CreateAPIView):
    serializer_class = VideoSerializer
    permission_class = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self, serializer):
        id = self.request.user.profile.school_id
        queryset = SchoolVideo.objects.filter(id=id)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.school_video.first()
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = {
            'message': 'Video successfully Uploaded',
            'status': status.HTTP_201_CREATED,
            'headers': headers,
            'serializer': serializer.data
        }
        return Response(res)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile)
        # serializer.save(user=self.request.user.profile)


class DisplayVideo(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = SchoolVideo.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        id = self.request.user.id
        queryset = VideoSerializer.objects.filter(id=id)
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
        response = {
            'data': serializer.data,
            'message': 'Principal Data Successfully save',
            status: status.HTTP_201_CREATED,
            'headers': headers

        }

        return Response(response)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)


class DisplayPrincipalDetialView(generics.RetrieveAPIView):
    serializer_class = PrincipalDetails
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_querryset(self):
        queryset = PrincipalDetails.objects.filter(
            id=self.request.GET.get('user.id'))
        return queryset


class EnquiryView(generics.CreateAPIView):
    serializer_class = EnquirySerialiazer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Enquiry.objects.filter(id=self.GET.get('user.id'))
        return queryset


class ReviewAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permissions = [permissions.AllowAny]

    def get_queryset(self, serializer):
        querset = Review.objects.filter(id=self.GET.get('user.id'))
        return querset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile.review.first()
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = {
            'message': 'review has been successfully Submitted',
            'status': status.HTTP_201_CREATED,
            'serializer': serializer.data
        }
        return Response(res)

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.profile)


class DisplayReview(generics.RetrieveAPIView):
    serializer_class = ReviewSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Review.objects.filter(id=user_id)
        return queryset
