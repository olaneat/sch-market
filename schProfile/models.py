from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .constants import Gender, Type, Level
from register.models import CustomUser
import uuid
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(
        CustomUser, related_name='profile', on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_address = models.TextField()
    school_badge = models.ImageField(
        upload_to="assets/badge", blank=True, null=True)
    school_type = models.CharField(max_length=50, choices=Type)
    school_gender = models.CharField(max_length=20, choices=Gender)
    school_level = models.CharField(max_length=40, choices=Level)
    school_state = models.CharField(max_length=100)
    date_established = models.DateField(blank=True, null=True)
    school_curriculum = models.CharField(max_length=255)
    school_fees_range = models.CharField(max_length=255)
    extra_curriculum_activities = models.TextField()
    school_phone_number = models.CharField(max_length=25)
    school_email = models.EmailField()
    school_motto = models.CharField(max_length=255)
    school_website = models.URLField(blank=True, null=True)
    school_clubs = models.TextField()
    school_facilities = models.TextField()
    competitive_advantage = models.TextField(blank=True, null=True)
    awards_won = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('school_name', 'created',)
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Profile'

    def __str__(self):
        return self.school_name


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
