from django.db import models
import uuid


class Status(models.Model):
    active = models.BooleanField(default=True)

    def inative(self):
        self.active = False
        self.save()

    class Meta:
        abstract = True


class Company(Status):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=20, unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    integration_code = models.CharField(max_length=20)

    class Meta:
        ordering = ['cnpj', 'active']

    def __str__(self):
        return self.cnpj


class Department(Status):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost_center = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    integration_code = models.CharField(max_length=20)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='departments')

    class Meta:
        ordering = ['company', 'name', 'active']

    def __str__(self):
        return '%s - (%s)%s' % (self.company.cnpj, self.cost_center, self.name)


class Employee(Status):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    join_date = models.DateField()
    exit_date = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=100)
    integration_code = models.CharField(max_length=20)
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='employees')
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='employees'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ErpProvider(Status):
    erp_name = models.CharField(max_length=100)
    erp_url = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True
    )

    class Meta:
        ordering = ['erp_name']

    def __str__(self):
        return self.erp_name


class IntegrationHistory(models.Model):
    status = models.IntegerField(blank=True, default=200)
    integration_code = models.UUIDField(default=uuid.uuid1, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    erp_provider = models.ForeignKey(
        'ErpProvider',
        on_delete=models.CASCADE,
        related_name='integration_history'
    )

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '%i - %s' % (self.status, self.code)
