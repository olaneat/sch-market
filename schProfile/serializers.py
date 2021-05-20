from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import serializers
from django.core.files.base import ContentFile
from django.conf import settings
import imghdr
import base64
import six
import uuid
from .models import Profile
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


class schoolProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True)
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    email = serializers.CharField(source="user.email", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Profile
        fields = (
            "email",
            "id",
            "username",
            "school_name",
            "address",
            "badge",
            "gender",
            "level",
            "state",
            "curriculum",
            "extra_curriculum_activities",
            "website",
            "clubs",
            "school_phone_number",
            "school_type",
            "school_email",
            "school_facilities",
            "awards_won",
            "date_established",
            "school_fees_range",
            "motto"
        )

        def create(self, validated_data, instance=None):
            if "user" in validated_data:
                user = validated_data.pop("user")
            else:
                user = CustomUser.objects.create(**validated_data)
            profile, create_profile = Profile.objects.update_or_create(
                user=user, defaults=validated_data
            )
            return profile


def get_username(self, obj):
    return obj.user.username


def get_email(self, obj):
    return obj.user.email
