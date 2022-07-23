from django.contrib import admin
from .models import Order, ProductInOrder, ProductInBasket, CollectionOrder, ProductInCollectionOrder, Status
from modeltranslation.admin import TranslationAdmin


class StatusAdmin(TranslationAdmin):
    list_display = ['status']

    class Meta:
        model = Status


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class ProductInCollectionOrderInline(admin.TabularInline):
    model = ProductInCollectionOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


class CollectionOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CollectionOrder._meta.fields]
    inlines = [ProductInCollectionOrderInline]

    class Meta:
        model = CollectionOrder


class ProductInCollectionOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCollectionOrder._meta.fields]

    class Meta:
        model = ProductInCollectionOrder


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket


admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)
admin.site.register(CollectionOrder, CollectionOrderAdmin)
admin.site.register(ProductInCollectionOrder, ProductInCollectionOrderAdmin)

