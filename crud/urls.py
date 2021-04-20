from django.urls import path
from .views import index, users

app_name = 'crud'
urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
]
