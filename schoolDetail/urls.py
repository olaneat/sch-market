from django.urls import path
from .apiviews import DisplayGalleryApi, GalleryApi, CreateAdmissionLetter, DisplayAdmissionLetter, DisplayVideo, SchoolVideoAPi

app_name = 'sch-detail'
urlpatterns = [
    path('create-gallery', GalleryApi.as_view(), name="create-gallery"),
    path('display-gallery', DisplayGalleryApi.as_view(), name='display-gallery'),
    path('create-video', SchoolVideoAPi.as_view(), name="create-video"),
    path('display-video', DisplayVideo.as_view(), name='display-video'),
    path('create-admission-letter', CreateAdmissionLetter.as_view(), name="addmission-letter"),
    path('display-addmission', DisplayAdmissionLetter.as_view(), name='display-admission-letter'),
]
