from django import forms
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    information = models.CharField(max_length=1000)
    Brand = models.ForeignKey(Brand,
                              on_delete=models.PROTECT,
                              related_name='Brand')

    rating = models.ImageField(default=0)


    def __str__(self):
        return '{brand} {name}'.format(
            brand = self.Brand,
            name = self.name,
        )

class Gallery(models.Model):
    image = models.ImageField(ulpoad_to='gallery')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')

class Colors(models.Model):
    color = forms.TextInput(attrs={'type': 'color'})
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='colors')

    def __str__(self):
        return self.color

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_public = models.DateTimeField()
    text_review = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Reviews')

    def __str__(self):
        return '{name} {lastname}'.format(name=self.name,
                                          lastname=self.last_name)
class Brand(models.Model):
    brand_name = models.CharField(max_length=200)