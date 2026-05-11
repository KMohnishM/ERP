from django.db import models
from django.conf import settings

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey('organizations.Department', on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)

class LeaveRequest(models.Model):
    TYPE_CHOICES = [('CASUAL', 'Casual'), ('SICK', 'Sick'), ('PAID', 'Paid')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='PENDING') # Integrated with Workflow module
