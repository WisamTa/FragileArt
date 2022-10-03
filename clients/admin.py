from django.contrib import admin
from .models import Client

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'business_type',
        'description',
        'image',
    )

admin.site.register(Client, ClientAdmin)

from django.contrib import admin
from .models import StudentData
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class StudentResource(resources.ModelResource):
      class Meta:
         model = StudentData

class StudentAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(StudentData,StudentAdmin)
