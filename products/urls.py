from django.urls import path
from products.views import addProduct

urlpatterns = [
    path('new/', addProduct)
]
