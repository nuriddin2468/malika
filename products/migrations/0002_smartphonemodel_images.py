# Generated by Django 2.2.1 on 2019-05-27 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infodb', '0002_imagesforproductsmodel'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphonemodel',
            name='images',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='infodb.ImagesForProductsModel', verbose_name='Фото'),
        ),
    ]