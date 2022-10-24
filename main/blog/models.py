from django.db import models
from django.urls import reverse

from main import settings


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Автор')
    title = models.CharField(max_length=300, default=None)
    image = models.ImageField(help_text='830x390', upload_to='BlogImages')
    data_publish = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=400, unique=True, db_index=True, verbose_name="URL", default=None)
    descr = models.CharField(max_length=1000, null=True, blank=True, default=None)
    author_desc = models.CharField(max_length=500, null=True, blank=True, default=None)

    class Meta:
        verbose_name = ('Пост')
        verbose_name_plural = ('Посты блога')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
