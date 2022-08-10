from django.db import models

# Create your models here.

class ProductTable(models.Model):
    ProductName = models.CharField(max_length=50) 
    ProductDesctiption = models.TextField()
    PRICE = models.IntegerField(null=True,blank=True)
    # STATUS = models.IntegerField

    def __str__(self):
        return self.ProductName

class Columns(models.Model):
    ProductId = models.ForeignKey(ProductTable,on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    CustomerName = models.CharField(max_length=50)
    CustomerEmail = models.EmailField(max_length=100)