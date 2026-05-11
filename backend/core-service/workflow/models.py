from django.db import models
from django.conf import settings

class WorkflowDefinition(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    trigger_event = models.CharField(max_length=100) # e.g., 'PURCHASE_REQUEST_CREATED'
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WorkflowStep(models.Model):
    workflow = models.ForeignKey(WorkflowDefinition, related_name='steps', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    label = models.CharField(max_length=255)
    assigned_role = models.CharField(max_length=100) # Role required to approve
    required_approvals = models.PositiveIntegerField(default=1)

class WorkflowInstance(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),
    ]
    workflow = models.ForeignKey(WorkflowDefinition, on_delete=models.PROTECT)
    resource_id = models.CharField(max_length=100) # ID of the object being approved
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    started_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    current_step = models.ForeignKey(WorkflowStep, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class WorkflowAction(models.Model):
    ACTION_CHOICES = [
        ('APPROVE', 'Approve'),
        ('REJECT', 'Reject'),
        ('COMMENT', 'Comment'),
    ]
    instance = models.ForeignKey(WorkflowInstance, related_name='actions', on_delete=models.CASCADE)
    step = models.ForeignKey(WorkflowStep, on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
