from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ('Name','Currency','Amount','TransactionDate')

