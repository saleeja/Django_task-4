from django.contrib import admin
from .models import Employee,Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'job_location', 'email', 'phone_number')
    search_fields = ('name', 'position', 'job_location', 'email', 'phone_number')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
