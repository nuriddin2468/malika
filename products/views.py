from django.shortcuts import render
from .form import *
# Create your views here.


def addProduct(request):
    form = SmartPhoneModelForm
    return render(request, 'test.html', {'form': form})
