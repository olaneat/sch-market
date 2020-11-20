from rest_framework import serializers
from .models import schoolProfile
from register.models import CustomUser

class SchoolProfileSerializer(serializers.ModelSerializer):
  username = serializers.CharField(read_only=True,  source='user.username')
  id= serializers.IntegerField(source='pk', read_only=True)
  email = serializers.CharField(source="user.email", read_only=True)
  school = serializers.CharField(read_only=True, source="user.username")


  class Meta:
    model = schoolProfile
    fields = ('school', 'id', 'username',  'email','school_name',
              'school_tel', 'school_type', 'school_address',
              'extral_curriculum_activities', 'intro_video',
              'school_curriculum', 'state', 'schoolfees_range',
              'school_email', 'school_badge', 'school_gender',

    )

  def get_schoolName(self,obj):
    return self.obj.school_name

  def get_badge(self, obj):
    if obj.badge:
      return obj.badge

''' 
  def create(self, validated_data, instance=None):
    if 'school' in validated_data:
      school = validated_data.pop('school')
    else:
      school = CustomUser.objects.create(**validated_data)
    profile, created_profile = schoolProfile.objects.update_or_create(school=school, **validated_data)
    return profile
'''
  