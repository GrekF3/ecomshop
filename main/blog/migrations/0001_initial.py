# Generated by Django 4.1.2 on 2022-10-23 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=300)),
                ('image', models.ImageField(help_text='830x390', upload_to='BlogImages')),
                ('data_publish', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default=None, max_length=400, unique=True, verbose_name='URL')),
                ('descr', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('author_desc', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты блога',
            },
        ),
    ]
