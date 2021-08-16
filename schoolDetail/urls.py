from os import name
from django.urls import path
from .apiviews import (DisplayGalleryApi, GalleryApi, SendMail,
                       RetrieveAdmissionForm, EnquiryView, DisplayVideo, SchoolVideoAPi,
                       DownAdmission, DisplayPrincipalDetialView, ReviewAPIView, DisplayReview,
                       CreatePrincipalDetailView, updatePrincipalDetail, create_review)

app_name = 'sch-detail'
urlpatterns = [
    path('create-gallery', GalleryApi.as_view(), name="create-gallery"),
    path('display-gallery', DisplayGalleryApi.as_view(), name='display-gallery'),
    path('create-video', SchoolVideoAPi.as_view(), name="create-video"),
    path('display-video', DisplayVideo.as_view(), name='display-video'),
    path('create-principal-detail', CreatePrincipalDetailView.as_view(),
         name="create-principal-detail"),
    path('display_principal_detail/<int:pk>', DisplayPrincipalDetialView.as_view(),
         name='display_prinicipa_detail'),
    path('create-enquiry', EnquiryView.as_view(), name="create_enquiry"),
    path('display-addmission', RetrieveAdmissionForm.as_view(),
         name='display-admission-letter'),
    path('add-review/<int:school_pk>',
         ReviewAPIView.as_view(),  name="add-review"),
    path('display-review', DisplayReview.as_view(), name="display-review"),
    path('update-prinicipal-detail/<int:pk>', updatePrincipalDetail.as_view(),
         name="update-principal_detail"),
    path('download-addmission/<int:pk>',
         DownAdmission.as_view(), name='download'),
    path('send-mail', SendMail.as_view(), name='send-mail'),
    path('<int:pk>/create-review', create_review, name='create-review')
]
