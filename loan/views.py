from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CustomerSerializer, CustomerHomeAddressSerializer, CustomerOfficeAddressSerializer, \
    LoanAmountDataSerializer, BranchDataSerializer
from .models import Customer, CustomerHomeAddress, CustomerOfficeAddress, LoanAmountData, BranchData, ExcelFileUpload


class LoanAmountDataSerializerViewSet(viewsets.ModelViewSet):
    queryset = LoanAmountData.objects.all()
    serializer_class = LoanAmountDataSerializer


class BranchDataSerializerViewSet(viewsets.ModelViewSet):
    queryset = BranchData.objects.all()
    serializer_class = BranchDataSerializer


class CustomerOfficeAddressSerializerViewSet(viewsets.ModelViewSet):
    queryset = CustomerOfficeAddress.objects.all()
    serializer_class = CustomerOfficeAddressSerializer


class CustomerHomeAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerHomeAddress.objects.all()
    serializer_class = CustomerHomeAddressSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


import pandas as pd
from django.conf import settings
import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser


class ExportImportExcel(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        obj = Customer.objects.all()
        serializer = CustomerSerializer(obj, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv", encoding="UTF-8", index=False)
        return Response({'status': 200})

    def post(self, request, *args, **kwargs):
        print("DATA!!!", request.data)
        print("FILE!!!", request.FILES)
        exceled_upload_obj = ExcelFileUpload.objects.create(excel_file_upload=request.FILES['files'])
        df = pd.read_csv(f"{settings.BASE_DIR}/public/static/{exceled_upload_obj.excel_file_upload}")
        print(df.values.tolist())
        for Customer in (df.values.tolist()):
            print(Customer)
            Customer.object.create(
                CustomerName=Customer[1],
                fatherName=Customer[3])
            print(Customer)

        return Response({'status': 200})
