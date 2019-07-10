from django.contrib import admin
from products.models import *
from .form import SmartPhoneModelForm
# Register your models here.


@admin.register(SmartPhoneModel)
class SmartPhoneAdmin(admin.ModelAdmin):
    form = SmartPhoneModelForm
    search_fields = ['name']
    list_display_links = ('name',)
    list_display = ('id', 'name', 'user', 'category', 'price')


@admin.register(CategoriesModel)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display_links = ('name',)
    list_display = ('id', 'name', 'idx')


