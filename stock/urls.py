from django.urls import path
from .views import sell_product


app_name = 'stock'
urlpatterns = [
    path('sell/<int:product_id>/', sell_product, name='sell_product'),
]
