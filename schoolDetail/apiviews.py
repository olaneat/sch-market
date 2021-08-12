from os import stat
from django.dispatch.dispatcher import receiver
from django.urls import conf
from rest_framework import generics
from .serializers import GallerySerializer, AdmissionFormSerializer, VideoSerializer, ReviewSerializer, PricipalDetailSerialiazer, EnquirySerialiazer
from rest_framework.response import Response
from schProfile.models import Profile
from rest_framework import status
from .utils import Utils
from wsgiref.util import FileWrapper
from django.http import Http404, HttpResponse
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import Gallery, Admission, SchoolVideo, PrincipalDetails, Review
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


class updatePrincipalDetail(generics.UpdateAPIView):
    serializer_class = PricipalDetailSerialiazer
    parser_classes = (MultiPartParser, FormParser)
    queryset = PrincipalDetails.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        display_image = PricipalDetailSerialiazer(data=request.data)
        if display_image.is_valid():
            display_image.save()
            response = {
                'message': 'Details successfully Updated',
                'status': status.HTTP_200_OK,
                'success': 'Ok'
            }
            return Response(response, display_image.data)
        else:
            return Response(display_image.errors)


class DisplayPrincipalDetialView(generics.RetrieveAPIView):
    serializer_class = PrincipalDetails
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
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
    queryset = Review.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
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
        print(self.request.kwargs)
        print(self.request.args)

        try:
            profile = Profile.objects.get(pk=self.request.user.profile.id)
            print(profile)
        except Profile.DoesNotExist:
            raise Http404
        if self.request.user.is_authenticated():
            serializer.save(user=profile)
        serializer.save()

    '''
  
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data
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
        id = self.request
        serializer.save(school=self.request.user.profile.id)
    
    get_queyset(self):
        profile = self.request.user.profile
        queryset = Review.objects.filter(user=profile)
        return queryset
    '''


class DisplayReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permissions = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    '''
    def get_queryset(self):
        user_id = self.request.user.profile_id
        queryset = Review.objects.filter(id=user_id)
        return queryset
    '''


class DownAdmission(generics.RetrieveAPIView):
    def get(self, request, id, format=None):
        queryset = Gallery.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        res = HttpResponse(FileWrapper(document),
                           content_type='application/msword')
        res['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return res


class SendMail(generics.GenericAPIView):
    serializer_class = EnquirySerialiazer

    def post(self, request):
        review = request.data

        serializer = self.serializer_class(data=review)
        serializer.is_valid(raise_exception=True)
        #review.data = serializer.data
        recipient = review['recipient_email']
        subject = review['subject']
        body = review['body'] + '\n' + review['contact_email']
        data = {
            'recipient': recipient,
            'subject': subject,
            'body': body
        }
        print(data)
        Utils.send_mail(data)
        res = {
            'message': 'Message Sent Successfully',
            'status': status.HTTP_200_OK,
            'code': 'OK',
            'data': serializer.data
        }
        return Response(res)


'''
class SendMail(generics.GenericAPIView):
    permissions = [permissions.AllowAny]

    def send_mail(self, template_id,  sender, recipient, data_dict):
        mail = Mail()
        mail.template_id = template_id
        mail.from_sender = Email(sender)
        personalization = Personalization
        personalization.add_to(Email(recipient))
        personalization.dynamic_template_data = data_dict
        mail.add_personilization(personalization)

        try:
            response = sg.client.mail.send.post(request_body=mail.get())
        except exceptions.BadRequestsError as e:
            print('now')
            print(e.body)
            exit()
            print(response.status_code)
            print(response.header)

    def post(self, request):
        recipient_email = request.data['recipient_email']
        subject = request.data['title']
        full_name = request.data['name']
        contact_email = request.data['contact_email']
        body = request.data['message']
        template_id = "d-1772e8ac6b5442e68975394ea71a4957"
        sender = 'olaneat2@gmail.com'
        data_dict = {'recipient_email': recipient_email, 'subject': subject, 'full_name': full_name,
                     'contact_email': contact_email, 'body': body}
        SendMail.send_mail(self, template_id, sender, recipient_email, data_dict)
        return Response({'status': status.HTTP_200_OK, 'message': 'message successfully sent'})
'''
