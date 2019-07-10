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
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    name = models.CharField(max_length=120, verbose_name="Название")
    price = models.FloatField(max_length=30, verbose_name="Цена")
    category = models.ForeignKey(CategoriesModel, verbose_name="Категория" ,on_delete=models.CASCADE)
    # Экран
    typeOfDisplay = models.ForeignKey(TypeOfDisplayModel, on_delete=models.CASCADE)
    diagonal = models.FloatField(max_length=10, verbose_name="Диагональ экрана")
    screenResolution = models.CharField(max_length=120, verbose_name="Разрешение экрана", default=None)
    glassType = models.CharField(max_length=120, verbose_name="Тип стекла", default=None)
    frameless = models.BooleanField(default=True, verbose_name="Безмрамочный")
    # Мультимедия
    cameraResolution = models.CharField(max_length=120, verbose_name="Разрешение фотокамеры", default=None)
    autofocus = models.BooleanField(default=True, verbose_name="Автофокусировка")
    flash = models.BooleanField(default=True, verbose_name="Встроенная вспышка")
    frontCamera = models.CharField(max_length=120, verbose_name="Фронтальная камера", default=None)
    dualCamera = models.BooleanField(default=True, verbose_name="Двойная камера")
    maximumVideoResolution = models.CharField(max_length=120, verbose_name="Максимальное разрешение видеосъемки", default=None)
    # Питание
    batteryMount = models.BooleanField(default=True, verbose_name="Крепление аккумулятора")
    wirelessCharger = models.BooleanField(default=False, verbose_name="Беспроводная зарядка")
    batteryCapacity = models.FloatField(max_length=30, verbose_name="Емкость аккумулятора", default=None)
    typeOfCharging = models.ForeignKey(TypeOfChargingModel, verbose_name="Тип разъема для зарядки", on_delete=models.CASCADE)
    # Дополнительная информация
    warranty = models.FloatField(max_length=30, verbose_name="Гарантия")
    manufacturer = models.ForeignKey(CountryModel, verbose_name="Изготовитель", on_delete=models.CASCADE, default=None)
    features = models.CharField(max_length=240, verbose_name="Особенности", default=None)
    color = models.CharField(max_length=120, verbose_name="Цвет")
    # Общие характеристики
    os = models.ForeignKey(OperatingSystemModel, verbose_name="Операционная система", on_delete=models.CASCADE, default=None)
    osVersion = models.CharField(max_length=120, verbose_name="Версия ОС", default=None)
    shellVersion = models.CharField(max_length=120, verbose_name="Версия оболочки", default=None)
    numOfSimCards = models.IntegerField(verbose_name="Количество SIM-карт", default=None)
    formatOfSimCards = models.CharField(max_length=120, verbose_name="Формат SIM-карты", default=None)
    material = models.ForeignKey(MaterialModel, verbose_name="Материал корпуса", on_delete=models.CASCADE, default=None)
    waitingTime = models.IntegerField(verbose_name="Время ожидания", default=None)
    talkTime = models.IntegerField(verbose_name="Время разговора", default=None)
    headphoneJack = models.BooleanField(default=True, verbose_name="Разъем для наушников")
    voiceControl = models.BooleanField(default=True, verbose_name="Голосовое управление")
    series = models.CharField(max_length=120, verbose_name="Серия", default=None)
    releaseYear = models.IntegerField(verbose_name="Год релиза", default=None)
    # Память и процессор
    internalMemory = models.IntegerField(verbose_name="Объём встроенной памяти", default=None)
    ramSize = models.IntegerField(verbose_name="Объём оперативной памяти", default=None)
    memoryCardSlot = models.BooleanField(default=True, verbose_name="Слот для карты памяти")
    maxMemoryCardCapacity = models.IntegerField(verbose_name="Максимальный объём карты памяти", default=None)
    cpu = models.ForeignKey(CPUModel, verbose_name="Процессор", on_delete=models.CASCADE)
    cpuModel = models.CharField(max_length=120, verbose_name="Модель процессора", default=None)
    processorCores = models.IntegerField(verbose_name="Количество ядер процессора", default=None)
    cpuFrequency = models.IntegerField(verbose_name="Частота процессора", default=None)
    videocpu = models.CharField(max_length=120, verbose_name="Видеопроцессор")
    # Связь
    bluetooth = models.BooleanField(default=True, verbose_name="Bluetooth")
    bluetoothStandart = models.CharField(max_length=120, verbose_name="Стандарт Bluetooth", default=None)
    g4 = models.BooleanField(default=True, verbose_name="4G LTE")
    diapg4 = models.CharField(max_length=120, verbose_name="Диапазоны 4G LTE", default=None)
    wifi = models.BooleanField(default=True, verbose_name="WI-FI")
    g3 = models.BooleanField(default=True, verbose_name="Поддержка 3G")
    nfc = models.BooleanField(default=False, verbose_name="Поддержка NFC")
    g5 = models.BooleanField(default=False, verbose_name="5G")
    # Функции
    gps = models.BooleanField(default=True, verbose_name="GPS-модуль")
    glonass = models.BooleanField(default=True, verbose_name="ГЛОНАСС")
    accelerometer = models.BooleanField(default=True, verbose_name="Акселерометр")
    sensors = models.CharField(max_length=240, verbose_name="Датчики", default=None)
    fingerprint = models.BooleanField(default=True, verbose_name="Сканер отпечатков пальцев")
    contactless = models.BooleanField(default=False, verbose_name="Бесконтактная технология оплаты")
    protection = models.BooleanField(default=False, verbose_name="Стандарт защита от пыли и влаги")
    faceUnlock = models.BooleanField(default=False, verbose_name="Разблокировка по лицу")
    # Габариты и вес
    weight = models.FloatField(max_length=30, verbose_name="Вес")
    height = models.FloatField(max_length=30, verbose_name="Высота", default=None)
    thickness = models.FloatField(max_length=30, verbose_name="Толщина")
    width = models.FloatField(max_length=30, verbose_name="Ширина")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Смартфоны и Планшеты"
        verbose_name_plural = "Смартфоны и Планшеты"


class SmartPhoneImageModel(models.Model):
    idx = models.ForeignKey(SmartPhoneModel, verbose_name="Название", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Фото")
