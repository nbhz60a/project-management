from django.db import models
from django.utils import timezone

class Tenant(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('Move-In', 'Move-In Coordination'),
        ('Construction', 'Construction Oversight'),
        ('Tenant-Liaison', 'Tenant Liaison'),
    ]
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, blank=True)
    vendors = models.ManyToManyField(Vendor, blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Leased', 'Leased'),
        ('Owned', 'Owned'),
    ]
    address = models.CharField(max_length=300)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES)

    def __str__(self):
        return self.address

class MaintenanceTask(models.Model):
    FREQUENCY_CHOICES = [
        ('Quarterly', 'Quarterly'),
        ('Bi-Annual', 'Bi-Annual'),
        ('Annual', 'Annual'),
    ]
    description = models.CharField(max_length=200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='maintenance_tasks')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    next_due_date = models.DateField()
    completed = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description


class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='leases')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField(blank=True)

    def __str__(self):
        return f"Lease for {self.tenant} at {self.property}"

class Document(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    upload_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
