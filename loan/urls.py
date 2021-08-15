from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ExportImportExcel

router = routers.DefaultRouter()
router.register('Customer', views.CustomerViewSet, basename='custmar')
router.register('CustomerHomeAddress', views.CustomerHomeAddressViewSet, basename='Cust Home Address')
router.register('CustomerOffice', views.CustomerOfficeAddressSerializerViewSet, basename='Cust Office Address')
router.register('Branch', views.BranchDataSerializerViewSet, basename='Branch Details')
router.register('loan', views.LoanAmountDataSerializerViewSet, basename='Loan details    ')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('excel/', ExportImportExcel.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
