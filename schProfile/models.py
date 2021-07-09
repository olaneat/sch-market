from django.contrib.contenttypes.fields import GenericRelation
import uuid
from register.models import CustomUser
from .constants import Gender, Type, Level
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete, post_save
from django.db import models
<< << << < HEAD
== == == =
>>>>>> > 2f4cfbf406b598cc5aa87d71708a0f9f6ca7f6b0
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


<< << << < HEAD
motto = models.CharField(max_length=255)
 website = models.URLField(blank=True, null=True)
  clubs = models.TextField()
   school_facilities = models.TextField
== == == =
school_motto = models.CharField(max_length=255)
 school_website = models.URLField(blank=True, null=True)
  school_clubs = models.TextField()
   school_facilities = models.TextField()
>>>>>> > 2f4cfbf406b598cc5aa87d71708a0f9f6ca7f6b0
awards_won = models.TextField()
 created = models.DateTimeField(auto_now=True)
  updated = models.DateTimeField(auto_now_add=True)

   class Meta:
        ordering = ('school_name', 'created',)
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Profile'

    def __str__(self):
        return self.school_name
<< << << < HEAD


@receiver(post_save, sender=CustomUser)
def create_school_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

== == == =


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):


>>>>>> > 2f4cfbf406b598cc5aa87d71708a0f9f6ca7f6b0
instance.profile.save()
