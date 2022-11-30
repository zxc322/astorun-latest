from django.db import models
from collection.models import Collection
from .const import GENDER_CHOICES, SIZE_CHOICES


class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, default=None, blank=True, null=True)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, default=None, blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name='Название')
    slug = models.SlugField(max_length=128, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    main_image = models.ImageField(upload_to='product_img/', verbose_name='Изображение', default='333')
    in_stock = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=None, verbose_name='Раздел')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return "id={}, title={}, price='{}'".format(self.id, self.title, self.price)

    class Meta:
        ordering = ['id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='product_img/', verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return 'imageId:{} => to ProductId{}'.format(self.product_id, self.id)


class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default=0)

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self):
        return 'pr_name: {}, size: {}'.format(self.product_id, self.size)


class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    color_name = models.CharField(max_length=20, default='white')

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.color_name


class ProductCategory(models.Model):
    category = models.CharField(max_length=15)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category
