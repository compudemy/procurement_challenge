# urls.py
from django.urls import path
from .views import manual_entry, best_product_view

app_name = 'backend'
urlpatterns = [
    path('manual-entry/', manual_entry, name='manual_entry'),
    path('best-product/', best_product_view, name='best_product'),
]
