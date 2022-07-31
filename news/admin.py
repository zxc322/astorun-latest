from django.contrib import admin
from .models import News, NewsImages
from modeltranslation.admin import TranslationAdmin


class NewsImageInline(admin.TabularInline):
    model = NewsImages
    extra = 0


class NewsAdmin(TranslationAdmin):

    list_display = ['id', 'title', 'slug']
    search_fields = ['title']
    inlines = [NewsImageInline]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)
