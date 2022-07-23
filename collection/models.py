from django.db import models
from django.db.models import BooleanField

from order.const import STATUS_CHOICES, DELIVERY_REGIONS


class Collection(models.Model):
    collection_name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True, db_index=True, verbose_name='URL')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='collection_img/', verbose_name='Изображение коллекции')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.collection_name


