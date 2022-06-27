from import_export import resources
from .models import Company

class CompanyResource(resources.ModelResource):
    class meta:
        model = Company