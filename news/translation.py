from modeltranslation.translator import register, TranslationOptions
from .models import News


@register(News)
class DocumentationTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)
