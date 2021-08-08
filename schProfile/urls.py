from django.urls import path
from . import apiviews
from .apiviews import CreateProfileView, UpdateSchoolProfile, DeleteSchoolProfile, DispaySchoolDetail, DisplaySchoolList, AdmissionDownload

app_name = 'profile'
urlpatterns = [
    path('create', CreateProfileView.as_view(), name='create-profile'),
    path('list', DisplaySchoolList.as_view(), name='school-list'),
    path('detail/<int:pk>', DispaySchoolDetail.as_view(), name='detail'),
    path('download/<int:id>', AdmissionDownload.as_view(), name='download'),
    path('update/<int:pk>', UpdateSchoolProfile.as_view(), name="update-profile"),
    path('delete/<int:pk>', DeleteSchoolProfile.as_view(), name="delete_profile"),
]
