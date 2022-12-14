# Generated by Django 4.1.2 on 2022-10-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_city_user_city_rename_country_user_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, choices=[('Краснодар', 'Краснодар')], max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, choices=[('Россия', 'Россия')], max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, choices=[('Краснодарский край', 'Краснодарский край')], max_length=255, verbose_name='Регион'),
        ),
    ]
