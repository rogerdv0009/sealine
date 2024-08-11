from django.contrib import admin
from .models import Team
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class TeamResource (resources.ModelResource):
    class Meta:
        model = Team

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','job']
    list_display = ('name','created_date','state')
    resource_class = TeamResource