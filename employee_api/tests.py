from django.test import TestCase
from .models import Company


class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Company.objects.create(
            cnpj='12345678901234',
            street='123 Main St',
            city='San Francisco',
            country='USA',
            integration_code='COMP123',
            active=True
        )

    def test_company_str_representation(self):
        company = Company.objects.get(id=1)
        expected_str = '12345678901234'
        self.assertEqual(str(company), expected_str)

    def test_company_is_active(self):
        company = Company.objects.get(id=1)
        self.assertTrue(company.active)

    def test_company_has_integration_code(self):
        company = Company.objects.get(id=1)
        self.assertIsNotNone(company.integration_code)
