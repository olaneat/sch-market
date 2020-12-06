from django.db import models
from register.models import CustomUser

class Admission(models.Model):
  school = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
  letter = models.FileField(upload_to='sch-detail/addmission-leta')


class Gallery(models.Model):
  school = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  picture =models.FileField(upload_to='sch-detail/sch-gallery')


  class Meta:
    verbose_name = 'School Gallery'
    verbose_name_plural = ' School Galleries'
    ordering = ('-school',)

  
