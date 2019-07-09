from django.db import models

# Create your models here.


class CountryModel(models.Model):
    nameEN = models.CharField(max_length=120, default="", verbose_name="Название на английском")
    nameRU = models.CharField(max_length=120, verbose_name="Название на русском")
    nameUZ = models.CharField(max_length=120, default="", verbose_name="Название на узбекском")

    def __str__(self):
        return self.nameEN

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class EthernetTypeModel(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Тип интернета"
        verbose_name = "Тип интернета"


class UsbTypeModel(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип USB"
        verbose_name_plural = "Типы USB"


class ImagesForProductsModel(models.Model):
    alt = models.CharField(verbose_name="Название фото", max_length=120)
    image1 = models.ImageField(verbose_name="Фото-1", default=None)
    image2 = models.ImageField(verbose_name="Фото-2", default=None)
    image3 = models.ImageField(verbose_name="Фото-3", default=None)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = "Фото для Продуктов"
        verbose_name = "Фото для продукта"
