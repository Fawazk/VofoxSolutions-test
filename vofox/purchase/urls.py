from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductList,name='ProductList'),
    path('productdetails',views.productdetails,name='productdetails'),
    path('orderslist',views.OrdersList,name='OrdersList'),
    path('addcolumns',views.AddColumns,name='AddColumns'),
    path('addproduct',views.addproduct,name='addproduct'),
    ]