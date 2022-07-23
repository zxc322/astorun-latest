from django.contrib import admin
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['collection_name', 'image', 'is_active']
    prepopulated_fields = {'slug': ('collection_name',)}

    class Meta:
        model = Collection


admin.site.register(Collection, CollectionAdmin)
