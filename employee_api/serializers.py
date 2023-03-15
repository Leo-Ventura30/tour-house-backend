from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import Company, Department, Employee, ErpProvider, IntegrationHistory


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['company', 'department', 'id', 'name', 'email', 'phone',
                  'birth_date', 'join_date', 'exit_date', 'integration_code', 'active']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        employees = EmployeeSerializer(many=True)

        model = Department
        fields = ['company', 'name', 'cost_center',
                  'integration_code', 'active', 'employees']


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        departments = DepartmentSerializer(many=True)

        model = Company
        fields = ['cnpj', 'street', 'city', 'integration_code',
                  'country', 'active', 'departments']


class ErpProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ErpProvider
        fields = '__all__'


class IntegrationHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IntegrationHistory
        fields = '__all__'
