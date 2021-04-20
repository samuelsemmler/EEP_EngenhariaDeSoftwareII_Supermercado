from django.urls import path
from .views import suppliers_list, supplier_detail, supplier_add, supplier_remove, supplier_update

app_name = 'suppliers'
urlpatterns = [
    path('', suppliers_list, name='suppliers_list'),
    path('<int:supplier_id>/', supplier_detail, name='supplier_detail'),
    path('add/', supplier_add, name='supplier_add'),
    path('update/<int:supplier_id>/', supplier_update, name='supplier_update'),
    path('remove/<int:supplier_id>/', supplier_remove, name='supplier_remove'),
]

