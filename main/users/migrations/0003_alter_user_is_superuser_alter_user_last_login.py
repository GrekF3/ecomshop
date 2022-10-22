# Generated by Django 4.1.2 on 2022-10-22 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_city_user_country_user_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Пользователь имеет все разрешения без явного их обозначения.', verbose_name='Суперпользователь'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последний вход'),
        ),
    ]
