from django.db import models
from django.urls import reverse


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    Androind = models.BooleanField(default=None)
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)
    banner = models.ImageField(upload_to='brand_baner', default=None)


    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return reverse('brand', kwargs={'brand_slug':self.slug})

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    information = models.CharField(max_length=1000)
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              related_name='Brand')

    rating = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(max_length=100, default=None)
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)
    price = models.DecimalField(default=0, max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug':self.slug})

    def __str__(self):
        return '{brand} {name} {color}'.format(
            brand=self.brand,
            name=self.name,
            color=self.color,
        )


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', help_text='270x300')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')

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

    def __str__(self):
        return self.title
