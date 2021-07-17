from django.db import models
from register.models import CustomUser


class Admission(models.Model):
    school = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    letter = models.FileField(upload_to='sch-detail/addmission-leta')

    def __str__(self):
        return self.school.username


class Gallery(models.Model):
    school = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    picture = models.FileField(upload_to='sch-detail/sch-gallery')

    class Meta:
        verbose_name = 'School Gallery'
        verbose_name_plural = ' School Galleries'
        ordering = ('-school',)

    def __str__(self):
        return self.school.username


class SchoolVideo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    intro_video = models.FileField(
        upload_to='assets/videos', blank=True, null=True)

    class Meta:
        ordering = ('-user',)

    def __str__(self):
        return self.school.username


class PrincipalDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    principal_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    display_image = models.FileField(
        upload_to='assests/principal', blank=True, null=True)
    post_held = models.CharField(max_length=255)

    class Meta:
        ordering = ('-user',)

    def __str__(self):
        return self.principal_name


class Enquiry(models.Model):
    title = models.CharField(max_length=255)
    sender_email = models.EmailField()
    enquiry = models.TextField()

    class Meta:
        ordering = ['-title']

        def __str__(self):
            return self.title
