from django.urls import path
from .apiviews import CreateProfileView, UpdateSchoolProfile, DeleteSchoolProfile, DispaySchoolDetail, DisplaySchoolList

app_name = 'profile'
urlpatterns = [
    path('create', CreateProfileView.as_view(), name='create-profile'),
    path('list', DisplaySchoolList.as_view(), name='school-list'),
    path('update', UpdateSchoolProfile.as_view(), name="update-profile")
]
