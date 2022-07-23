# Generated by Django 3.2.9 on 2022-07-18 01:04

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='URL')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('main_image', models.ImageField(default='333', upload_to='product_img/', verbose_name='Изображение')),
                ('in_stock', models.BooleanField(default=True)),
                ('gender', models.CharField(choices=[('man', 'Men'), ('woman', 'Women'), ('kid', 'Kids')], default=None, max_length=10, verbose_name='Раздел')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
                ('category_en', models.CharField(max_length=15, null=True)),
                ('category_ru', models.CharField(max_length=15, null=True)),
                ('category_uk', models.CharField(max_length=15, null=True)),
                ('slug', models.SlugField(max_length=15, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('UniSize', 'Universal Size'), ('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Two Extra Large')], default=0, max_length=20)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='product_img/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(default='white', max_length=20)),
                ('color_name_en', models.CharField(default='white', max_length=20, null=True)),
                ('color_name_ru', models.CharField(default='white', max_length=20, null=True)),
                ('color_name_uk', models.CharField(default='white', max_length=20, null=True)),
                ('color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.collection'),
        ),
    ]
