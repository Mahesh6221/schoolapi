from django.contrib import admin

from api.models import School, Student

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name','location','type',)
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','school',)
    list_filter = ('school',)


admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)

# mahesh
# mahesh@gmail.com
# Mahesh@123