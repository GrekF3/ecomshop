from django import forms
from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    Androind = models.BooleanField(default=None)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    information = models.CharField(max_length=1000)
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='Brand')

    rating = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=100, default=None)

    def __str__(self):
        return '{brand} {name} {color}'.format(
            brand = self.brand,
            name = self.name,
            color = self.color,
        )

class Gallery(models.Model):

    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='gallery')

    def __str__(self):
        return self.product.name

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_public = models.DateTimeField()
    text_review = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Reviews')

    def __str__(self):
        return '{name} {lastname}'.format(name=self.name,
                                          lastname=self.last_name)

class Ad(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Ads_product')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='ads', help_text='800x600')