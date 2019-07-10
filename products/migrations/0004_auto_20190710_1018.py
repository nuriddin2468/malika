# Generated by Django 2.2.3 on 2019-07-10 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infodb', '0004_cpumodel_materialmodel_operatingsystemmodel_typeofchargingmodel_typeofdisplaymodel'),
        ('products', '0003_auto_20190709_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='cameraresol',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='cores',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='diaphragm',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='display',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='ethernet',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='externalMemory',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='focus',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='frequency',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='garant',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='images',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='mass',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='pixil',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='sim',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='simCount',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='system',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='usb',
        ),
        migrations.RemoveField(
            model_name='smartphonemodel',
            name='zoom',
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='accelerometer',
            field=models.BooleanField(default=True, verbose_name='Акселерометр'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='autofocus',
            field=models.BooleanField(default=True, verbose_name='Автофокусировка'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='batteryCapacity',
            field=models.FloatField(default=None, max_length=30, verbose_name='Емкость аккумулятора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='batteryMount',
            field=models.BooleanField(default=True, verbose_name='Крепление аккумулятора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='bluetoothStandart',
            field=models.CharField(default=None, max_length=120, verbose_name='Стандарт Bluetooth'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='cameraResolution',
            field=models.CharField(default=None, max_length=120, verbose_name='Разрешение фотокамеры'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='contactless',
            field=models.BooleanField(default=False, verbose_name='Бесконтактная технология оплаты'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='cpuFrequency',
            field=models.IntegerField(default=None, verbose_name='Частота процессора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='cpuModel',
            field=models.CharField(default=None, max_length=120, verbose_name='Модель процессора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='diapg4',
            field=models.CharField(default=None, max_length=120, verbose_name='Диапазоны 4G LTE'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='dualCamera',
            field=models.BooleanField(default=True, verbose_name='Двойная камера'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='faceUnlock',
            field=models.BooleanField(default=False, verbose_name='Разблокировка по лицу'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='features',
            field=models.CharField(default=None, max_length=240, verbose_name='Особенности'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='fingerprint',
            field=models.BooleanField(default=True, verbose_name='Сканер отпечатков пальцев'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='flash',
            field=models.BooleanField(default=True, verbose_name='Встроенная вспышка'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='formatOfSimCards',
            field=models.CharField(default=None, max_length=120, verbose_name='Формат SIM-карты'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='frameless',
            field=models.BooleanField(default=True, verbose_name='Безмрамочный'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='frontCamera',
            field=models.CharField(default=None, max_length=120, verbose_name='Фронтальная камера'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='g3',
            field=models.BooleanField(default=True, verbose_name='Поддержка 3G'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='g4',
            field=models.BooleanField(default=True, verbose_name='4G LTE'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='g5',
            field=models.BooleanField(default=False, verbose_name='5G'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='glassType',
            field=models.CharField(default=None, max_length=120, verbose_name='Тип стекла'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='glonass',
            field=models.BooleanField(default=True, verbose_name='ГЛОНАСС'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='gps',
            field=models.BooleanField(default=True, verbose_name='GPS-модуль'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='headphoneJack',
            field=models.BooleanField(default=True, verbose_name='Разъем для наушников'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='height',
            field=models.FloatField(default=None, max_length=30, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='internalMemory',
            field=models.IntegerField(default=None, verbose_name='Объём встроенной памяти'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='manufacturer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='infodb.CountryModel', verbose_name='Изготовитель'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='material',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='infodb.MaterialModel', verbose_name='Материал корпуса'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='maxMemoryCardCapacity',
            field=models.IntegerField(default=None, verbose_name='Максимальный объём карты памяти'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='maximumVideoResolution',
            field=models.CharField(default=None, max_length=120, verbose_name='Максимальное разрешение видеосъемки'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='memoryCardSlot',
            field=models.BooleanField(default=True, verbose_name='Слот для карты памяти'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='numOfSimCards',
            field=models.IntegerField(default=None, verbose_name='Количество SIM-карт'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='os',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='infodb.OperatingSystemModel', verbose_name='Операционная система'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='osVersion',
            field=models.CharField(default=None, max_length=120, verbose_name='Версия ОС'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='processorCores',
            field=models.IntegerField(default=None, verbose_name='Количество ядер процессора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='protection',
            field=models.BooleanField(default=False, verbose_name='Стандарт защита от пыли и влаги'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='ramSize',
            field=models.IntegerField(default=None, verbose_name='Объём оперативной памяти'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='releaseYear',
            field=models.IntegerField(default=None, verbose_name='Год релиза'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='screenResolution',
            field=models.CharField(default=None, max_length=120, verbose_name='Разрешение экрана'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='sensors',
            field=models.CharField(default=None, max_length=240, verbose_name='Датчики'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='series',
            field=models.CharField(default=None, max_length=120, verbose_name='Серия'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='shellVersion',
            field=models.CharField(default=None, max_length=120, verbose_name='Версия оболочки'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='talkTime',
            field=models.IntegerField(default=None, verbose_name='Время разговора'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='thickness',
            field=models.FloatField(default=1, max_length=30, verbose_name='Толщина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='typeOfCharging',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='infodb.TypeOfChargingModel', verbose_name='Тип разъема для зарядки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='typeOfDisplay',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='infodb.TypeOfDisplayModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='videocpu',
            field=models.CharField(default=1, max_length=120, verbose_name='Видеопроцессор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='voiceControl',
            field=models.BooleanField(default=True, verbose_name='Голосовое управление'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='waitingTime',
            field=models.IntegerField(default=None, verbose_name='Время ожидания'),
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='warranty',
            field=models.FloatField(default=1, max_length=30, verbose_name='Гарантия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='weight',
            field=models.FloatField(default=1, max_length=30, verbose_name='Вес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='width',
            field=models.FloatField(default=1, max_length=30, verbose_name='Ширина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphonemodel',
            name='wirelessCharger',
            field=models.BooleanField(default=False, verbose_name='Беспроводная зарядка'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='bluetooth',
            field=models.BooleanField(default=True, verbose_name='Bluetooth'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.CategoriesModel', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='color',
            field=models.CharField(max_length=120, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='cpu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infodb.CPUModel', verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='diagonal',
            field=models.FloatField(max_length=10, verbose_name='Диагональ экрана'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='nfc',
            field=models.BooleanField(default=False, verbose_name='Поддержка NFC'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='price',
            field=models.FloatField(max_length=30, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='smartphonemodel',
            name='wifi',
            field=models.BooleanField(default=True, verbose_name='WI-FI'),
        ),
        migrations.CreateModel(
            name='SmartPhoneImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('idx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SmartPhoneModel', verbose_name='Название')),
            ],
        ),
    ]