from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    organization = models.ForeignKey(Organization, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
