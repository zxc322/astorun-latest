from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory, ProductColor, Product


@register(ProductCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(ProductColor)
class ColorTranslationOptions(TranslationOptions):
    fields = ('color_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)