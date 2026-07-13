from django.urls import path
from .views import *

urlpatterns = [
    path('products/',AllProducts,name='all_products'),
    path('products/add/',AddProduct,name='add_product'),
    # path('products/edit/<int:id>',EditProduct,name='edit_product'),
    # path('products/delete/<int:id>',DeleteProduct,name='delete_product'),    
    
]
