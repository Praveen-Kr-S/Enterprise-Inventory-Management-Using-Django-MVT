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

def UpdateProduct(request,pk):
    edit_product = Product.objects.get(id=pk)
    edit_form = ProductForm(instance=edit_product)
    if request.method == 'POST':
        edit_form = ProductForm(request.POST,request.FILES,instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_products')
    return render(request,'add_product.html',{'edit_form':edit_form})

def DeleteProduct(request,id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect('all_products')