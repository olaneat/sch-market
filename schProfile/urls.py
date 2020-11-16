from .apiviews import ProfileListView, CreateProfileView, SchoolProfileDetailView, updateSchoolProfile, DeleteSchoolProfile
from django.urls import path

app_name = 'profile'
urlpatterns = [
    path('create', CreateProfileView.as_view(), name ='create_profile'),
    path('list', ProfileListView.as_view(), name='list_profile'),
    path('<int:pk>/delete', DeleteSchoolProfile.as_view(), name="delete_profile"),
    path('<int:pk>/detail',SchoolProfileDetailView.as_view(), name='profile_detail'),
    path('<int:pk>/update', updateSchoolProfile.as_view(), name='update_profile')

]
