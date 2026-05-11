from django.db import models

class ChartOfAccount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50) # Asset, Liability, Equity, Revenue, Expense
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    client_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    ledger = models.ForeignKey(ChartOfAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')])
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
