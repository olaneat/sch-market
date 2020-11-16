from rest_framework import serializers
from .models import schoolProfile

class SchoolProfileSerializer(serializers.ModelSerializer):
  username = serializers.CharField(read_only=True, max_length=255, )
  class Meta:
    model = schoolProfile
    exclude = 'user'

  def create(self, validate_data, instance=None):
    if 'user' in validated_data:
      user = validated_data.pop('user')
    else:
      user = CustomUser.objects.create(**validated_data)
    profile, create_profile = CustomUser.objects.update_or_create(user=user, **validated_data)
    return profile

    def get_schoolName(self,obj):
      return self.obj.schoolName

    def get_badge(self, obj):
      if obj.badge:
        return obj.badge
