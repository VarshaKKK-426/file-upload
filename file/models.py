from django.db import models

# Create your models here.
class Company(models.Model):
    Name = models.CharField(max_length=50, null=True)
    Currency = models.CharField(max_length=3)
    Amount = models.DecimalField(max_digits=8, decimal_places=2)
    TransactionDate = models.DateField(auto_now_add=True)


    