from modeltranslation.translator import register, TranslationOptions
from .models import Documentation


@register(Documentation)
class DocumentationTranslationOptions(TranslationOptions):
    fields = ('text',)