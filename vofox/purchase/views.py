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
    context = {
        'productdetails': productdetails,
    }
    return render(request, 'ProductDetails.html', context)

def AddColumns(request):
    ProductId = request.GET.get('id')
    form = OrderForm(request.POST)
    if form.is_valid():
        order = Columns()
        order.ProductId = ProductId
        order.Quantity = form.cleaned_data['Quantity']
        order.CustomerName = form.cleaned_data['CustomerName']
        order.CustomerEmail = form.cleaned_data['CustomerEmail']
        order.save()
    return redirect(OrdersList)

def addproduct(requset):
    form = ProductForm(requset.POST)
    if form.is_valid():
        product = ProductTable()
        product.ProductName = form.cleaned_data['ProductName']
        product.ProductDesctiption = form.cleaned_data['ProductDesctiption']
        product.save()
    return redirect(ProductList)
