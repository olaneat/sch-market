from rest_framework import serializers
from .models import schoolProfile
from register.models import CustomUser

class SchoolProfileSerializer(serializers.ModelSerializer):
  username = serializers.CharField(read_only=True, max_length=255, source='user.username')
  id= serializers.IntegerField(source='pk', read_only=True)
  user = serializers.CharField(read_only=True, source="user.username")

  class Meta:
    model = schoolProfile
    fields = ('user', 'id', 'username',  'schoolName',
              'school_tel', 'school_type', 'school_address',
              'extral_curriculum_activities', 'intro_video',
              'school_curriculum', 'state', 'schoolfees_range',
              'school_email', 'school_badge', 'school_gender',

    )

  def create(self, validated_data, instance=None):
    if 'user' in validated_data:
      user = validated_data.pop('user')
    else:
      user = CustomUser.objects.create(**validated_data)
    profile, created_profile = schoolProfile.objects.update_or_create(user=user, **validated_data)
    return profile

    def get_schoolName(self,obj):
      return self.obj.schoolName

    def get_badge(self, obj):
      if obj.badge:
        return obj.badge
