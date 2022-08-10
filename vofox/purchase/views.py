from email import message
from django.shortcuts import redirect, render
from .models import ProductTable,Columns
from .form import OrderForm,ProductForm
# Create your views here.

def ProductList(request):
    products = ProductTable.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

def OrdersList(request):
    orders = Columns.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders.html', context)

def productdetails(request):
    ProductId = request.GET.get('id')
    productdetails = ProductTable.objects.get(id=ProductId)
    form = OrderForm()
    context = {
        'productdetails': productdetails,
        'form':form,
    }
    return render(request, 'ProductDetails.html', context)

def AddColumns(request):
    ProductId = request.GET.get('id')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Columns()
        order.Quantity = form.cleaned_data['Quantity']
        order.ProductId = ProductTable.objects.get(id=ProductId)
        order.CustomerName = form.cleaned_data['CustomerName']
        order.CustomerEmail = form.cleaned_data['CustomerEmail']
        order.save()
        return redirect(OrdersList)
    return redirect(ProductList)

def addproduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = ProductTable()
            product.ProductName = form.cleaned_data['ProductName']
            product.ProductDesctiption = form.cleaned_data['ProductDesctiption']
            product.save()
        return redirect(ProductList)
    context={
        'form':form,
    }
    return render(request, 'aadproduct.html', context)
