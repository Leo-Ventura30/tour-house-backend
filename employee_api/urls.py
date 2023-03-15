from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import CompanyViewSet, DepartmentViewSet, EmployeeViewSet, ErpProviderViewSet, IntegrationHistoryViewSet

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)
router.register('companies', CompanyViewSet)
router.register('provider', ErpProviderViewSet)
router.register('integracao/erp/employees', IntegrationHistoryViewSet)

urlpatterns = [
    path('login/', obtain_auth_token),
    path('', include(router.urls)),
]
