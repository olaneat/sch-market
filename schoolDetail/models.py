from register.models import CustomUser
from django.db import models
from schProfile.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


class PrincipalDetails(models.Model):
    user = models.OneToOneField(
        Profile, related_name='principal_detail', on_delete=models.CASCADE)
    principal_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    display_image = models.FileField(
        upload_to='assests/principal')
    post_held = models.CharField(max_length=255)

    class Meta:
        ordering = ('-principal_name',)

    def __str__(self):
        return self.principal_name


@receiver(post_save, sender=Profile)
def create_principal_detail(sender, instance, created, **kwargs):
    if created:
        principal_detail = PrincipalDetails.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def save_principal_detail(sender, instance, **kwargs):
    instance.principal_detail.save()


class Admission(models.Model):
    school = models.ForeignKey(
        Profile, related_name='admission',  on_delete=models.CASCADE)
    admission_form = models.FileField(upload_to='sch-detail/addmission-leta')

    def __str__(self):
        return self.school.username


class Gallery(models.Model):
    school = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='gallery')
    picture = models.FileField(upload_to='assets/sch-gallery')

    class Meta:
        verbose_name = 'School Gallery'
        verbose_name_plural = ' School Galleries'
        ordering = ('-school',)

    def __str__(self):
        return self.school.school_name


class SchoolVideo(models.Model):
    school = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='school_video')
    intro_video = models.FileField(
        upload_to='assets/videos', blank=True, null=True)

    ''' 
    class Meta:
        ordering = ('-school',)
    '''

    def __str__(self):
        return self.school.school_name


class Review(models.Model):
    school = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='review')
    name = models.CharField(max_length=250, blank=True, null=True )
    rating = models.CharField(
        max_length=250, blank=True, null=True)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
