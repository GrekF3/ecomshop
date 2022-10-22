from django.db import models
from django.urls import reverse

from main import settings


class Brand(models.Model):
    brand_name = models.CharField(max_length=200,verbose_name='Бренд')
    Androind = models.BooleanField(default=None, verbose_name='Андроид')
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)
    brand_logo = models.ImageField(upload_to='brand_logos', help_text='270x300', default='default',verbose_name='Лого Бренда')



    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_slug':self.slug})

    class Meta:
        verbose_name = ('Бренд')
        verbose_name_plural = ('Бренды')

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя продукта')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    information = models.CharField(max_length=1000, verbose_name='Информация')
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='Brand', verbose_name='Бренд')

    rating = models.PositiveSmallIntegerField(default=0, verbose_name='Рейтинг')
    color = models.CharField(max_length=100, default=None, verbose_name='Цвет')
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)
    price = models.DecimalField(default=0, max_digits=20, decimal_places=2, verbose_name='Цена')

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug':self.slug})

    def __str__(self):
        return '{brand} {name} {color}'.format(
            brand=self.brand,
            name=self.name,
            color=self.color,
        )
    class Meta:
        verbose_name = ('Товар')
        verbose_name_plural = ('Товары')


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', help_text='270x300')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')
    class Meta:
        verbose_name = ('Фото')
        verbose_name_plural = ('Фотографии')

    def __str__(self):
        return self.product.name


class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True,blank=True)
    data_public = models.DateTimeField(verbose_name='Дата отзыва')
    text_review = models.CharField(max_length=255,verbose_name='Отзыв')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Reviews', verbose_name='Товар')

    def __str__(self):
        return '{name} {product}'.format(name=self.user,
                                          product=self.product)

    class Meta:
        verbose_name = ('Отзыв')
        verbose_name_plural = ('Отзывы')


class Ad(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Ads_product', verbose_name='Товар')
    title = models.CharField(max_length=50, verbose_name='Главный текст')
    description = models.CharField(max_length=255, verbose_name='Нижний текст')
    photo = models.ImageField(upload_to='ads', help_text='800x600', verbose_name='Баннер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Банер')
        verbose_name_plural = ('Рекламные банеры')
