from django.urls import path
from .apiviews import CreateProfileView, UpdateSchoolProrfile, DeleteSchoolProfile, DispaySchoolDetail, DisplaySchoolList

app_name = 'profile'
urlpatterns = [
    path('create', CreateProfileView.as_view(), name='create-profile'),
    path('list', DisplaySchoolList.as_view(), name='scrhool-list')
]
