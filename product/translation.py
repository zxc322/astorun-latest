from modeltranslation.translator import register, TranslationOptions
from .models import ProductCategory, ProductColor


@register(ProductCategory)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)


@register(ProductColor)
class ColorTranslationOptions(TranslationOptions):
    fields = ('color_name',)
