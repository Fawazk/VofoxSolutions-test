from django.db.models import fields
from django.forms import ModelForm
from .models import ProductTable,Columns
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = ProductTable
        fields = ['ProductName','ProductDesctiption']


    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
              
              
class OrderForm(forms.ModelForm):
    class Meta:
        model = Columns
        fields = ['Quantity', 'CustomerName', 'CustomerEmail']

    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'