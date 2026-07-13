from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

def AllProducts(request):
    products = Product.objects.all()
    return render(request,'all_products.html',{'products':products})


def AddProduct(request):
    add_form = ProductForm()
    if request.method == 'POST':
        add_form = ProductForm(request.POST,request.FILES)
        if add_form.is_valid():
            add_form.save()
            return redirect('all_products')
    return render(request,'add_product.html',{'add_form':add_form})