from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Gallery, Admission, SchoolVideo, PrincipalDetails, Review, Enquiry
from schProfile.models import Profile


class GallerySerializer(serializers.ModelSerializer):
    school = serializers.CharField(
        source='gallery.school_name', read_only=True)

    class Meta:
        model = Gallery
        fields = ('picture')


class AdmissionFormSerializer(serializers.ModelSerializer):
    school = serializers.CharField(
        source='admission.school_name', read_only=True)

    class Meta:
        model = Admission
        fields = ('admission_form')


class VideoSerializer(serializers.ModelSerializer):
    school = serializers.CharField(
        source="school_video.school_name", read_only=True)

    class Meta:
        model = SchoolVideo
        fields = ('intro_video')


class ReviewSerializer(serializers.ModelSerializer):
    school = serializers.CharField(
        source="review.school_name", read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'review', 'reviewer_email')


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


class EnquirySerialiazer(serializers.ModelSerializer):
    school = serializers.CharField(
        source="enquiry.school_name", read_only=True)

    class Meta:
        model = Enquiry
        fields = ('title', 'sender_email', 'enquiry')
