from django.contrib import admin
from .models import (
    Tenant,
    Vendor,
    Project,
    Task,
    Property,
    MaintenanceTask,
    Lease,
    Document,
)

admin.site.register(Tenant)
admin.site.register(Vendor)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Property)
admin.site.register(MaintenanceTask)
admin.site.register(Lease)
admin.site.register(Document)
