from rest_framework import serializers

from .models import Customer, CustomerHomeAddress, CustomerOfficeAddress, BranchData, LoanAmountData


class BranchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchData
        fields = ("__all__")


class LoanAmountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmountData
        fields = ("__all__")


class CustomerHomeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerHomeAddress
        fields = ("__all__")


class CustomerOfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOfficeAddress
        fields = ("__all__")


class CustomerSerializer(serializers.ModelSerializer):
    CustHome = CustomerHomeAddressSerializer(many=True, read_only=True)
    CustOffice = CustomerOfficeAddressSerializer(many=True, read_only=True)
    CustLoan     = LoanAmountDataSerializer(many=True, read_only=True)
    CustBranch = BranchDataSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['customer_name', 'father_name', 'customer_profile', 'loan_account_no', 'CustBranch',
                  'CustHome', 'CustOffice', 'CustLoan']
