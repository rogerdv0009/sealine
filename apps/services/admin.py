from django.contrib import admin
from .models import Service
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ServiceResource (resources.ModelResource):
    class Meta:
        model = Service

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','created_date','state')
    resource_class = ServiceResource