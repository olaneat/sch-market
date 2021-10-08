from datetime import datetime
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .serializers import SearchSerializer, schoolProfileSerializer
from rest_framework import filters
from rest_framework.views import APIView
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
#from schoolDetail.serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from .models import Profile
from rest_framework import generics
#from schoolDetail.models import Review

'''
    class CustomSearchFilter(filters.SearchFilter):
        def get_search_fields(self, view, request):
            if request.query_params.get('title_only'):
                return ['title']
            return super(CustomSearchFilter, self).get_search_fields(view, request)
'''


class CreateProfileView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, instance=request.user.profile
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers

        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    '''

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

  def post(self, request):
    
    file_upload = schoolProfileSerializer(data =request.data, instance=request.user)
    if file_upload.is_valid():
      file_upload.save()
      return Response(file_upload.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_upload.errors, status=status.HTTP_400_BAD_REQUEST )

  
  '''


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class SchoolSearch(generics.ListAPIView):
    filter_backends = (filters.SearchFilter,)
    serializer_class = SearchSerializer
    search_fields = ['school_name', 'school_state']
    queryset = Profile.objects.all()


class DisplaySchoolList(generics.ListAPIView):
    queryset = Profile.objects.exclude(school_name='')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = schoolProfileSerializer

    '''
        search_fields = ['school_name', 'school_state',
                     'school_address', 'school_fees_range']
        #filter_backends = (filters.SearchFilter,)
    '''


class DispaySchoolDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()
    today = datetime.now().day
    starting_month = 'Aug'
    current_month = datetime.today().strftime('%B')
    print(current_month)

    if today > 1 and starting_month == current_month:
        starting_month = current_month
        print('halo')
        print(today)
    print(starting_month)

    #print('today\'s date is ' + today + current_month)


class UpdateSchoolProfile(generics.UpdateAPIView):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = schoolProfileSerializer

    def post(self, request):
        badge = schoolProfileSerializer(data=request.data)
        if badge.is_valid():
            badge.save()
            response = {
                'message': 'Profile successfully created',
                'status': status.HTTP_200_OK,
                'success': True
            }
            return Response(badge.data, response)
        else:
            return Response(badge.errors,  status=status.HTTP_400_BAD_REQUEST)


class DeleteSchoolProfile(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()


'''
@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny])
def school_detail(request, id, **validated_data):
    profile = Profile.objects.filter(id=id)
    #reviews = Review.objects.all()
    new_review = True
    if request.method == 'POST':
        serializer = schoolProfileSerializer(data=request.data)
        if serializer.is_valid():
            new_review = serializer.save(**validated_data)
            #new_review = serializer.save(commit=False)
            new_review.review = profile
            new_review.save()
    else:
        new_review = ReviewSerializer()

    res = {
        'message': 'review Added successfully',
        'success': 'OK',
        'status': status.HTTP_200_OK,
        'serializer': serializer.data
    }
    return Response(res)

'''

class AdmissionDownload(generics.RetrieveAPIView):
    def get(self, request, id,  format=None, **kwargs):
        queryset = super().get_context_data(**kwargs)
        instance = self.get_object()
        #queryset = Profile.gallery(id=id)
        file_handle = instance.file.path
        document = open(file_handle, 'rb')
        res = HttpResponse(FileWrapper(document),
                           content_type='application/msword')
        res['Content-Disposition'] = 'attachment; filename"%s"' % queryset.file.name
        return res
