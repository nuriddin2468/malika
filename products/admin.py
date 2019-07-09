from django.contrib import admin
from products.models import *
from .form import SmartPhoneModelForm
# Register your models here.


@admin.register(SmartPhoneModel)
class SmartPhoneAdmin(admin.ModelAdmin):
    form = SmartPhoneModelForm
    search_fields = ['name']
    list_display_links = ('name',)
    list_display = ('id', 'name', 'user', 'category', 'country', 'price')
    list_filter = ('country', )
    fieldsets = (
        (None, {
           'fields': ('name', ('user', 'category'), 'price', ('color', 'garant'), 'images')
        }),
        ('Связь', {
            'fields': ('ethernet', ('bluetooth', 'wifi'), ('usb', 'nfc'))
        }),
        ('Дисплей', {
            'fields': ('display', ('diagonal', 'resolution'), 'sensor')
        }),
        ('Фотокамера', {
            'fields': (('pixil', 'diaphragm'), ('zoom', 'focus'), 'cameraresol')
        }),
        ('Процессор', {
            'fields': (('cpu', 'cores'), 'frequency')
        }),
        ('Память', {
            'fields': ('ram', ('memory', 'externalMemory'))
        }),
        ('Сим-карта', {
            'fields': (('sim', 'simCount'),)
        }),
        ('Система', {
            'fields': (('system', 'mass'),)
        }),
        ('Питание', {
            'fields': ('capacity',)
        })
    )


@admin.register(CategoriesModel)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display_links = ('name',)
    list_display = ('id', 'name', 'idx')


