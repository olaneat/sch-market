from django.contrib import admin
from .models import schoolProfile

@admin.register(schoolProfile)
class SchoolProfileAdmin(admin.ModelAdmin):
  fields = ['school_name', 'school_email']
  search_fields = ['email', 'school_name']

# Register your models here.
