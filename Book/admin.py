from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models  import  Book

# Register your models here.


# class Book(ImportExportModelAdmin, admin.ModelAdmin):
#     pass

admin.site.register(Book)