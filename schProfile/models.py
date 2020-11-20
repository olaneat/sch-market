from django.db import models
from  register.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save
from .constants import Gender, school_level, School_type


class schoolProfile(models.Model):
  school = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  school_name  = models.CharField(max_length=255, blank=True, null=True)
  school_badge = models.ImageField(upload_to='profile/badge', blank=True, null=True)
  school_gender = models.CharField(max_length=255, choices = Gender, blank=True, null=True)
  school_type = models.CharField(max_length=255, choices=School_type, blank=True, null=True)
  school_address = models.TextField(blank=True, null=True)
  extral_curriculum_activities = models.TextField(blank=True, null=True)
  intro_video = models.FileField(upload_to = 'profile/video', blank=True, null=True)
  state = models.CharField(max_length=255, blank=True, null=True)
  school_email = models.EmailField(max_length=254, blank=True, null=True)
  school_tel = models.CharField(max_length = 150, blank=True, null=True)
  school_curriculum = models.CharField(max_length=255, blank=True, null=True)
  schoolfees_range = models.CharField(max_length=255, blank=True, null=True)

  class Meta:
    verbose_name = 'School Profile'
    verbose_name_plural = 'School Profiles'
    ordering = ('-school_name',)
  
  def __str__(self):
      return self.schoolName
  


  @receiver(post_save, sender=CustomUser)
  def create_school_profile(sender, instance, created,**kwargs):
      if created:
        schoolProfile.objects.create(user=instance)

  @receiver(post_save, sender=CustomUser)
  def save_receiver(sender, created, instance, **kwargs):
    instance.schoolprofile.save()
    
  

@receiver(pre_delete, sender=CustomUser)
def delete_school_profile(sender, instance, **kwargs):
  if instance:
    school_profile = SchoolProfile.objects.get(user=instace)
    school_profile.delete()