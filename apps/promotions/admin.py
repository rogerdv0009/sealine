from django.contrib import admin
from .models import Promotion
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PromotionResource (resources.ModelResource):
    class Meta:
        model = Promotion

@admin.register(Promotion)
class PromotionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','created_date','state')
    resource_class = PromotionResource