from django.urls import path
from .apiviews import DisplayGalleryApi, GalleryApi, RetrieveAdmissionForm, DisplayVideo, SchoolVideoAPi, DisplayPrincipalDetialView, CreatePrincipalDetailView

app_name = 'sch-detail'
urlpatterns = [
    path('create-gallery', GalleryApi.as_view(), name="create-gallery"),
    path('display-gallery', DisplayGalleryApi.as_view(), name='display-gallery'),
    path('create-video', SchoolVideoAPi.as_view(), name="create-video"),
    path('display-video', DisplayVideo.as_view(), name='display-video'),
    path('create-principal-detail', CreatePrincipalDetailView.as_view(),
         name="create-principal-detail"),
    path('display_principal_detail', DisplayPrincipalDetialView.as_view(),
         name='display_prinicipa_detail'),
    path('display-addmission', RetrieveAdmissionForm.as_view(),
         name='display-admission-letter'),
]
