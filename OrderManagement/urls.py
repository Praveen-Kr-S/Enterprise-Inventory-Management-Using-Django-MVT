
from django.urls import path, include
from .views import *

urlpatterns = [
    path('customers/', All_Customers, name='all_customers'),
    path('customers/add/', Add_Customer, name='add_customer'),
    path('customers/edit/<int:id>/', Edit_Customer, name='edit_customer'),
    path('customers/delete/<int:id>/', Delete_Customer, name='delete_customer'),
]