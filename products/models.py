from django.db import models
from django.contrib.auth.models import User
from infodb.models import *
# Create your models here.


class CategoriesModel(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название")
    idx = models.IntegerField(verbose_name="ID категории", default=-1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"


class SmartPhoneModel(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="Название")
    price = models.FloatField(verbose_name="Цена")
    country = models.ForeignKey(CountryModel, verbose_name="Страна",default="", on_delete=models.CASCADE)
    category = models.ForeignKey(CategoriesModel, verbose_name="Категория", default="", on_delete=models.CASCADE)
    # Связь
    ethernet = models.ManyToManyField(EthernetTypeModel, verbose_name="Тип интернета")
    bluetooth = models.CharField(max_length=120, verbose_name="Версия блютуза")
    wifi = models.CharField(max_length=120, verbose_name="Версия вай-фая")
    nfc = models.BooleanField(verbose_name="NFC", default=False)
    usb = models.ForeignKey(UsbTypeModel, verbose_name="Тип USB", on_delete=models.CASCADE)
    # Дисплей
    display = models.CharField(max_length=120, verbose_name="Тип дисплея")
    diagonal = models.FloatField(verbose_name="Диагональ")
    resolution = models.CharField(max_length=120, verbose_name="Разрешение(300x200)")
    sensor = models.BooleanField(verbose_name="Сенсор", default=True)
    # Фотокамера
    pixil = models.CharField(max_length=120, verbose_name="Камеры в пиксилях (12 МП + 10 МП)")
    diaphragm = models.CharField(max_length=120, verbose_name="Диафрагмы ( F1.5/F2.4 + F2.2 )")
    zoom = models.BooleanField(verbose_name="Зум камеры", default=False)
    focus = models.BooleanField(verbose_name="Автофокус", default=False)
    cameraresol = models.CharField(max_length=120, verbose_name="Разрешение записи ( 200x300 + 400x500 )")
    # Процессор
    cpu = models.CharField(max_length=120, verbose_name="Процессор")
    cores = models.IntegerField(verbose_name="Количество ядер")
    frequency = models.CharField(max_length=120, verbose_name="Частота (2.4)")
    # Память
    ram = models.IntegerField(verbose_name="Озу")
    memory = models.IntegerField(verbose_name="Память")
    externalMemory = models.IntegerField(verbose_name="Внешняя память до")
    # Симкарта
    sim = models.CharField(max_length=30, verbose_name="Тип симкарты (Nano,Big)")
    simCount = models.IntegerField(verbose_name="Кол-во Сим-Карт")
    # Система
    system = models.CharField(max_length=120, verbose_name="Система")
    mass = models.FloatField(max_length=120, verbose_name="Вес(г)")
    # Питание
    capacity = models.IntegerField(verbose_name="Емкость акамулятора")
    garant = models.CharField(max_length=120, verbose_name="Гарантия")
    color = models.CharField(max_length=120, verbose_name="Цвета")
    images = models.ForeignKey(ImagesForProductsModel, verbose_name="Фото", default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Смартфоны и Планшеты"
        verbose_name_plural = "Смартфоны и Планшеты"



