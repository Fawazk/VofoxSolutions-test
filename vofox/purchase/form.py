from django.db.models import fields
from django.forms import ModelForm
from .models import ProductTable,Columns
from django import forms
class ProductForm(ModelForm):
    class Meta:
        model = ProductTable
        fields = ['ProductName','ProductDesctiption']
              
class OrderForm(forms.ModelForm):
    class Meta:
        model = Columns
        fields = ['Quantity', 'CustomerName', 'CustomerEmail']