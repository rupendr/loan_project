# Create your models here.
from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    customer_profile = models.CharField(max_length=12)
    loan_account_no = models.IntegerField()

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customer data"


class BranchData(models.Model):
    CustBranch= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustBranch")
    zone_name = models.CharField("Zone Name", max_length=12, )
    region_name = models.CharField("Region Name", max_length=12, )
    area_name = models.CharField("Area Name", max_length=12, )
    branch_name = models.CharField("Branch Name", max_length=12, )
    branch_code = models.CharField("Branch Code", max_length=12, )

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name = "Branch data"
        verbose_name_plural = "Branch data"


class CustomerHomeAddress(models.Model):
    CustHome= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustHome")
    pincode = models.CharField("ZIP / Postal code", max_length=12, )
    landmark = models.CharField("landmark", max_length=1024, )
    address1 = models.CharField("Address line 1", max_length=1024, )
    address2 = models.CharField("Address line 2", max_length=1024, )
    address3 = models.CharField("Address line 3", max_length=1024, )
    def __str__(self):
        return self.pincode

    class Meta:
        verbose_name = "Cust Home Address"
        verbose_name_plural = "Cust Home Address"



class CustomerOfficeAddress(models.Model):
    CustOffice= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustOffice")
    office_pincode = models.CharField("ZIP / Postal code", max_length=12, )
    office_landmark = models.CharField("landmark", max_length=1024, )
    office_address1 = models.CharField("Address line 1", max_length=1024, )
    office_address2 = models.CharField("Address line 2", max_length=1024, )
    office_address3 = models.CharField("Address line 3", max_length=1024, )
    def __str__(self):
        return self.office_pincode

    class Meta:
        verbose_name = "Cust office Address"
        verbose_name_plural = "Cust office Address"



class LoanAmountData(models.Model):
    CustLoan= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustLoan")
    agreement_date = models.CharField("AGREEMENT DATE ", max_length=12, )
    lrn = models.CharField("LRN", max_length=12, )
    tenor = models.CharField("TENOR", max_length=12, )
    adv_emi = models.CharField("ADV EMI", max_length=12, )
    mob = models.CharField("MOB", max_length=12, )
    def __str__(self):
        return self.agreement_date

    class Meta:
        verbose_name = "Loan amount data"
        verbose_name_plural = "Loan amount data"


class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")




