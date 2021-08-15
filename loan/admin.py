from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerHomeAddress, CustomerOfficeAddress, BranchData, LoanAmountData,ExcelFileUpload
admin.site.register(Customer)
admin.site.register(CustomerHomeAddress)
admin.site.register(CustomerOfficeAddress)
admin.site.register(BranchData)
admin.site.register(LoanAmountData)

admin.site.register(ExcelFileUpload)
