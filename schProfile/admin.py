from django.contrib import admin
from .models  import Profile

# Register your models here.
@admin.register(Profile )
class schoolProfileAdmin(admin.ModelAdmin):
  list_display=['school_name']
  search_fields = ['school_name', 'school_email']
