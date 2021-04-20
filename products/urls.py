from django.urls import path
from .views import products_list, product_add, product_details, product_remove, product_update

app_name = 'products'
urlpatterns = [
    path('', products_list, name='products_list'),
    path('add/', product_add, name='products_add'),
    path('details/<int:product_id>/', product_details, name='product_details'),
    path('update/<int:product_id>/', product_update, name='product_update'),
    path('remove/<int:product_id>/', product_remove, name='product_remove'),
]
