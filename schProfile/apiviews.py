from rest_framework import generics
from .models import Profile
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Profile
from .serializers import schoolProfileSerializer
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser


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
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
        print('profile created successfully')

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


class DisplaySchoolList(APIView):
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DispaySchoolDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()


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
            return Response(badge.data, status=status.HTTP_200_OK)
        else:
            return Response(badge.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSchoolProfile(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = schoolProfileSerializer
    queryset = Profile.objects.all()
