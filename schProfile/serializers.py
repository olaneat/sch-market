from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import serializers
from django.core.files.base import ContentFile
import imghdr
import base64
import six
import uuid
from .models import schoolProfile
from register.models import CustomUser


class Base64Imagefield(serializers.ImageField):
  
  def to_internal_value(self, data):
    if isinstance(self, six.string_types):
      if 'data: ' in data and ';base64, ' in data:
        header, data = data.split(';base64,')
      try:
        decode_file = base64.b64decode(data)
      except TypeError:
        self.fail('invalide image')

      file_name = str(uuid.uuid4())[:16]
      file_extension = self.get_file_extension(file_name, decode_file)
      complete_file_name = "%s.%s" %(file_name, file_extension)
      data = ContentFile(decode_file, name=complete_file_name)

    return super(Base64Imagefield, self).to_internal_value(data)  

  def get_file_extension(self, file_name, decode_file):
    extension = imghdr.what(file_name, decode_file)
    extension = 'jpg' if extension == 'jpeg' else extension

    return extension

class schoolProfileSerializer(serializers.ModelSerializer):
  parser_classes = (MultiPartParser, FormParser, )
  id = serializers.IntegerField(source='pk', read_only=True)
  email = serializers.CharField(source='user.email', read_only=True)
  username = serializers.CharField(source='user.username', read_only=True)
  badge = Base64Imagefield(max_length=None, use_url=True)

  class Meta:
    model = schoolProfile
    fields = ( 'email', 'id', 'username', 'school_name',
              'address', 'badge', 'gender', 'level',
              'state', 'curriculum', 'extra_curriculum_activities',
              'website', 'clubs', 'school_phone_number', 'school_type',
              'school_email', 'school_facilities', 'awards_won', 'date_established',
              'school_fees_range', 'motto'
    )

  def create(self, validated_data, instance=None):
    if 'user' in validated_data:
      user = validated_data.pop('user')
    else:
      user = CustomUser.objects.create(**validated_data)
    profile, created_profile = schoolProfile.objects.update_or_create(user=user, **validated_data)
    return profile
