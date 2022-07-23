from modeltranslation.translator import register, TranslationOptions
from .models import Status


@register(Status)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('status',)
