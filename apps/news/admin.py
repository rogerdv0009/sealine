from django.contrib import admin
from .models import New, Comment
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class NewResource (resources.ModelResource):
    class Meta:
        model = New

@admin.register(New)
class NewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','created_date','state')
    resource_class = NewResource


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['email','description']
    list_display = ('email','created_date','state')
    resource_class = CommentResource