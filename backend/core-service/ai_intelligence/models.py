from django.db import models

class AIAnalyticReport(models.Model):
    module_context = models.CharField(max_length=100) # e.g., 'Finance', 'HR'
    query_summary = models.TextField()
    insights_json = models.JSONField()
    generated_at = models.DateTimeField(auto_now_add=True)

class SmartRecommendation(models.Model):
    user_id = models.CharField(max_length=100)
    recommendation_type = models.CharField(max_length=100) # e.g., 'StockOptimization', 'BudgetAlert'
    content = models.TextField()
    confidence_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
