# Generated by Django 4.1.2 on 2022-10-17 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_colors_color_alter_gallery_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Color',
        ),
    ]