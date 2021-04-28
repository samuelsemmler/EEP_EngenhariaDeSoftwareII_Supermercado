from django.urls import path
from .views import index


app_name = 'teams'
urlpatterns = [
    path('', index, name='index'),
]
