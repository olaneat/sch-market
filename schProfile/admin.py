from django.contrib import admin
from .models import schoolProfile

@admin.register(schoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
  fields = ['schoolName', 'school_email']
  search_fields = ['email', 'schoolName']

# Register your models here.
