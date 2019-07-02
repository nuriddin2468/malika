from django.contrib import admin
from infodb.models import *
# Register your models here.


@admin.register(CountryModel)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ['nameRU', 'nameUZ', 'nameEN']


@admin.register(EthernetTypeModel)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(ColorTypeModel)
class ColorTypeAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display_links = ('name',)
    list_display = ('id', 'name', 'code')


@admin.register(UsbTypeModel)
class UsbTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ImagesForProductsModel)
class ImagesForProductsAdmin(admin.ModelAdmin):
    pass
