from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver 
from .constants import Gender, Type, Level
from register.models import CustomUser
# Create your models here.

class schoolProfile(models.Model):
  user = models.OneToOneField(CustomUser,related_name='school_profile', on_delete=models.CASCADE)
  school_name = models.CharField(max_length=255)
  address = models.TextField()
  badge = models.ImageField(upload_to='assets/badge', blank=True, null=True)
  school_type = models.CharField(max_length=50, choices=Type) 
  gender  = models.CharField(max_length=20, choices=Gender)
  level = models.CharField(max_length=40, choices=Level)
  state = models.CharField(max_length=100)
  date_established = models.DateTimeField(blank=True, null=True)
  curriculum = models.CharField(max_length= 255)
  school_fees_range = models.CharField(max_length=255)
  extra_curriculum_activities = models.TextField()
  school_phone_number = models.CharField(max_length=25)
  school_email = models.EmailField()
  motto = models.CharField(max_length=255)
  website = models.URLField( blank=True, null=True)
  clubs = models.TextField()
  school_facilities = models.TextField
  awards_won = models.TextField()
  created = models.DateTimeField(auto_now=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering  = ('school_name', 'created',)
    verbose_name = 'School Profile'
    verbose_name_plural = 'School Profile'

  def __str__(self):
      return self.school_name
  
  '''

    @receiver(post_save, sender=CustomUser)
    def create_update_profile(sender, instance=None, created=False, **kwargs):
      if created:
        schoolProfile.objects.get_or_create(user=instance)

    @receiver(post_save, sender=CustomUser)
    def save_profile(sender, instance=None, **kwargs):
      instance.profile.save()
  
   @receiver(pre_delete, sender=CustomUser)
  def delete_school_profile(self, sender, instance=None, **kwargs):
    if instance:
      profile = schoolProfile.objects.get(user = instance)
      profile.delete()
      
  '''



