from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['roll','reg','name','father','date_time']
    search_fields= ['roll']
    list_filter=['gender']
    list_editable = ['name']
admin.site.register(Student,StudentAdmin)
