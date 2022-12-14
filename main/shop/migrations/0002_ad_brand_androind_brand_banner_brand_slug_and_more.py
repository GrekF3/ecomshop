# Generated by Django 4.1.2 on 2022-10-17 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('photo', models.ImageField(help_text='800x600', upload_to='ads')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='Androind',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='brand',
            name='banner',
            field=models.ImageField(default=None, upload_to='brand_baner'),
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=None, max_length=400, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, max_length=400, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='shop.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Colors',
        ),
        migrations.AddField(
            model_name='ad',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ads_product', to='shop.product'),
        ),
    ]
