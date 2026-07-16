from django.urls import path
from .views import *

urlpatterns = [
    path('products/',AllProducts,name='all_products'),
    path('products/add/',AddProduct,name='add_product'),
    path('products/edit/<int:pk>/',UpdateProduct,name='update_product'),
    path('products/delete/<int:id>',DeleteProduct,name='delete_product'),    
    
]
