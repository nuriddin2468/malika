from django.db import models

# Create your models here.


class TypeOfDisplayModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Тип экрана")

    def __str__(self):
        return self.name


class TypeOfChargingModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Тип разъема для зарядки")

    def __str__(self):
        return self.name


class CountryModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Страна", default=None)

    def __str__(self):
        return self.name


class OperatingSystemModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Операционная система")

    def __str__(self):
        return self.name


class MaterialModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Материал")

    def __str__(self):
        return self.name


class CPUModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Процессор")

    def __str__(self):
        return self.name
