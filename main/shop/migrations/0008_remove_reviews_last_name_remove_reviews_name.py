# Generated by Django 4.1.2 on 2022-10-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_ad_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='name',
        ),
    ]
