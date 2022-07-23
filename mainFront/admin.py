from django.contrib import admin
from .models import Documentation
from modeltranslation.admin import TranslationAdmin


class DocumentationAdmin(TranslationAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Documentation


admin.site.register(Documentation, DocumentationAdmin)
