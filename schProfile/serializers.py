from django.db import models
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from schoolDetail.models import Gallery
from rest_framework import serializers
#from django.core.files.base import ContentFile
from django.conf import settings
import base64
import imghdr
import six
import uuid
from .models import Profile
from schoolDetail.serializers import PricipalDetailSerialiazer, EnquirySerialiazer, GallerySerializer, ReviewSerializer, VideoSerializer, AdmissionFormSerializer
from register.models import CustomUser


class Base64Imagefield(serializers.ImageField):

    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension)
            data = ContentFile(decoded_file, name=complete_file_name)
        return super(Base64Imagefield, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = 'jpg' if extension == 'jpeg' else extension

        return extension


class SearchSerializer(serializers.Serializer):
    school_name = serializers.CharField(max_length=255)


class schoolProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="user.id", read_only=True)
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    email = serializers.CharField(source="user.email", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)
    principal_detail = PricipalDetailSerialiazer(required=False)
    gallery = GallerySerializer(many=True, read_only=True)
    school_video = VideoSerializer(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    admission_form = AdmissionFormSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            "email",
            "id",
            "username",
            'competitive_advantage',
            "school_name",
            'admission_form',
            'principal_detail',
            'gallery',
            'school_video',
            'review',
            "school_address",
            "school_badge",
            "school_gender",
            "school_level",
            "school_state",
            "school_curriculum",
            "extra_curriculum_activities",
            "school_website",
            "school_clubs",
            "school_phone_number",
            "school_type",
            "school_email",
            "school_facilities",
            "awards_won",
            "date_established",
            "school_fees_range",
            "school_motto"
        )

    def create(self, validated_data, instance=None):
        if "user" in validated_data:
            user = validated_data.pop("user")
        else:
            user = CustomUser.objects.create(**validated_data)
        gallery = validated_data.pop('school_gallery')
        profile = Profile.objects.update_or_create(
            user=user, defaults=validated_data
        )
        return profile


def get_username(self, obj):
    return obj.user.username


def get_email(self, obj):
    return obj.user.email
