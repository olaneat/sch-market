from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Gallery, Admission, SchoolVideo, PrincipalDetails, Review, Enquiry
from schProfile.models import Profile


class PricipalDetailSerialiazer(serializers.ModelSerializer):
    school = serializers.CharField(
        source="principal_detail.school_name", read_only=True)

    class Meta:
        model = PrincipalDetails
        fields = ('id', 'principal_name', 'school', 'phone_number',
                  'post_held', 'display_image')

        def create(self, validated_data, instance=None):
            if 'user.profile' in validated_data:
                user = validated_data.pop('user.profile')
            else:
                user = Profile.objects.create(**validated_data)
            principal_detail = PrincipalDetails.objects.update_or_create(
                user=user, defaults=validated_data
            )
            return principal_detail


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('picture', 'id')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolVideo
        fields = ('intro_video',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('name',  'review', 'id', 'reviewer_email', 'rating')


class AdmissionFormSerializer(serializers.ModelSerializer):
    school = serializers.CharField(
        source='admission.school_name', read_only=True)

    class Meta:
        model = Admission
        fields = ('admission_form', 'school')


class EnquirySerialiazer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    body = serializers.CharField()
    recipient_email = serializers.EmailField()
    contact_email = serializers.EmailField()
