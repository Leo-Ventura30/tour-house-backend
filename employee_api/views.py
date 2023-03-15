from django.views.generic.detail import SingleObjectMixin
from rest_framework import viewsets, status, filters

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from .models import Company, Department, Employee, ErpProvider, IntegrationHistory
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, ErpProviderSerializer, IntegrationHistorySerializer


class StatusView(SingleObjectMixin):
    model = None

    def destroy(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.inative()
        return Response({'detail': f'{self.object} inativado'})


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['active',
                        'employees__department', 'employees']
    ordering_fields = ['cnpj', 'active']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['employees']
    ordering_fields = ['active']


class EmployeeViewSet(StatusView, viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['active', 'company', 'department', 'city']
    ordering_fields = ['active']


class ErpProviderViewSet(viewsets.ModelViewSet):
    queryset = ErpProvider.objects.filter()
    serializer_class = ErpProviderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['active', 'erp_name']
    ordering_fields = ['erp_name', 'active']


class IntegrationHistoryViewSet(viewsets.ModelViewSet):
    queryset = IntegrationHistory.objects.filter()
    serializer_class = IntegrationHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'created_at']
    ordering_fields = ['status', 'created_at']

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # employees = Employee.objects.all()

        # data = {
        #     "integration_code": response.data['integration_code'],
        #     "created_at": response.data['created_at'],
        #     "employees": employees
        # }

        # # Simulando a integração com o ERP, enviando os dados via HTTP
        # # substituir o endereço abaixo pelo endereço real do ERP

        # url = "http://meu-erp.com.br/integra-funcionarios/"
        # headers = {'Content-type': 'application/json'}
        # r = requests.post(url, data=json.dumps(data), headers=headers)

        # # Verifica se a integração foi bem sucedida

        # if r.status_code == 200:
        #     response.data['code'] = r.json()['code']
        #     response.data['created_at'] = r.json()['timestamp']
        #     response.status_code = status.HTTP_200_OK
        #     return response
        # else:
        #     response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        #     return response

        return response
