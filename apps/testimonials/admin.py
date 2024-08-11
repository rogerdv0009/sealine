from django.contrib import admin
from .models import Testimonial
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class TestimonialResource (resources.ModelResource):
    class Meta:
        model = Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','description']
    list_display = ('name','created_date','state')
    resource_class = TestimonialResource