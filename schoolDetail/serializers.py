from rest_framework import serializers
from .models import Gallery, Admission, SchoolVideo

class GallerySerializer(serializers.ModelSerializer):
  school = serializers.CharField(source='user.username', read_only=True)

  class Meta:
    model = Gallery
    fields = ('picture', 'school')

  
  class AdmissionFormSerializer(serializers.ModelSerializer):
    school = serializers.CharField(source='user.username', read_only=True)

    class Meta:
      model = Admission
      fields = ('school', 'letter')

  
class AdmissionSerializer(serializers.ModelSerializer):
  school=serializers.CharField(source='user.username', read_only=True)

  class Meta:
    model = Admission
    fields = ('school', 'letter')


class VideoSerializer(serializers.ModelSerializer):
  school = serializers.CharField(source="user.username", read_only=True)

  class Meta:
    model = SchoolVideo
    fields = ('school', 'intro_video')