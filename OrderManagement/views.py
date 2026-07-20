from django.shortcuts import redirect, render
from .models import *
from .forms import CustomerForm

def All_Customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers/all_customers.html', {'customers': customers})


def Add_Customer(request):
    add_form = CustomerForm()
    if request.method == 'POST':
        add_form = CustomerForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('all_customers')
    return render(request, 'customers/add_customer.html', {'add_form': add_form})


def Edit_Customer(request, id):
    customer = Customer.objects.get(id=id)
    edit_form = CustomerForm(instance=customer)
    if request.method == 'POST':
        edit_form = CustomerForm(request.POST, instance=customer)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('all_customers')
    return render(request, 'customers/add_customer.html', {'edit_form': edit_form})


def Delete_Customer(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('all_customers')