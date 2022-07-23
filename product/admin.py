from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductColorInline(admin.TabularInline):
    model = ProductColor
    extra = 0


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 0


class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'price', 'category', 'gender', 'collection', 'in_stock']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [ProductImageInline, ProductSizeInline, ProductColorInline]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']

    class Meta:
        model = ProductImage


class ProductCategoryAdmin(TranslationAdmin):
    list_display = ['category']
    prepopulated_fields = {'slug': ('category',)}

    class Meta:
        model = ProductCategory


class ProductColorAdmin(TranslationAdmin):
    list_display = ['color_name']

    class Meta:
        model = ProductColor


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
