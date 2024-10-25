from django.urls import path
from .views import index, success_view

app_name='frontend'
urlpatterns = [
    path('', index, name='index'),
    path('success/', success_view, name='success_url'),
]