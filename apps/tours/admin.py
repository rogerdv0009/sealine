from django.contrib import admin
from .models import Tour
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class TourResource (resources.ModelResource):
    class Meta:
        model = Tour

@admin.register(Tour)
class TourAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','created_date','state')
    resource_class = TourResource