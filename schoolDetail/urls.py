from django.urls import path
from .apiviews import DisplayGalleryApi, GalleryApi,  RetrieveAdmissionForm, EnquiryView, DisplayVideo, SchoolVideoAPi, DisplayPrincipalDetialView, ReviewAPIView, DisplayReview, CreatePrincipalDetailView, updatePrincipalDetail

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
    path('add-review', ReviewAPIView.as_view(),  name="add-review"),
    path('display-review', DisplayReview.as_view(), name="display-review"),
    path('update-prinicipal-detail/<int:pk>', updatePrincipalDetail.as_view(),
         name="update-principal_detail")

]
