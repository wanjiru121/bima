from django.contrib import admin
from common.models import County, SubCounty, Ward, Village, UnitAreaOfInsurance, InsuranceData
from import_export.admin import ImportExportModelAdmin
from .models import County, SubCounty, Ward, Village, InsuranceData
from import_export import resources
from django.http import HttpResponse
from .import_excel_to_model import import_excel_to_model

class InsuranceDataResource(resources.Resource):
    def import_data(self, dataset, dry_run=False, raise_errors=False,
                    use_transactions=None, collect_failed_rows=False,
                    **kwargs):
        result = import_excel_to_model(dataset)

        return HttpResponse("Import completed.")

class InsuranceDataAdmin(ImportExportModelAdmin):
    resource_class = InsuranceDataResource

# Register your models here.
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Ward)
admin.site.register(Village)
admin.site.register(UnitAreaOfInsurance)
admin.site.register(InsuranceData, InsuranceDataAdmin)




