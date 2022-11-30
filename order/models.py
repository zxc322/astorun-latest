from django.db import models
from product.models import Product
from django.db.models.signals import post_delete
from .const import DELIVERY_REGIONS


class Order(models.Model):
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    user = models.CharField(max_length=200, blank=True, null=True, default='user')
    order_price = models.IntegerField()
    delivery_price = models.IntegerField(null=True, default=0)
    customer_name = models.CharField(max_length=28)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=28)
    delivery_region = models.CharField(max_length=40, choices=DELIVERY_REGIONS, default=None)
    delivery_district = models.CharField(max_length=40, default=None, blank=True)
    delivery_city = models.CharField(max_length=40, default=None)
    nova_poshta_departament = models.SmallIntegerField(default=None)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return 'Order id =' + str(self.id)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    size = models.CharField(max_length=10, default='Universal')
    color = models.CharField(max_length=20, default='white', null=True)
    quantity = models.PositiveIntegerField(default=1)
    price_per_item = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Product in Order"
        verbose_name_plural = "Products in Order"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.quantity * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def post_delete_product_in_order(sender, instance, *args, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_active=True)
    order_price = 0
    for product in all_products_in_order:
        order_price += product.total_price

    instance.order.order_price = order_price
    instance.order.save(force_update=True)


post_delete.connect(post_delete_product_in_order, sender=ProductInOrder)


class ProductInBasket(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=140)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=20, default='white', null=True)
    price_per_item = models.IntegerField(default=0)
    product_total_price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return 'Product[{}], size={}'.format(self.product, self.size)

    class Meta:
        verbose_name = "Product in Basket"
        verbose_name_plural = "Products in Basket"

    # Calculating price for certain product to show it in cart

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.product_total_price = int(self.quantity) * int(self.price_per_item)

        super(ProductInBasket, self).save(*args, **kwargs)


# Order as collection

class CollectionOrder(models.Model):
    user = models.CharField(max_length=200, blank=True, null=True, default='user')
    order_price = models.IntegerField()
    discount_percent = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=28)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=28)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    delivery_region = models.CharField(max_length=40, choices=DELIVERY_REGIONS, default=None)
    delivery_district = models.CharField(max_length=40, default=None, blank=True)
    delivery_city = models.CharField(max_length=40, default=None)
    nova_poshta_departament = models.SmallIntegerField(default=None)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return 'ColOrder id =' + str(self.id)


class ProductInCollectionOrder(models.Model):
    col_order = models.ForeignKey(CollectionOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    size = models.CharField(max_length=10, default='Universal')
    color = models.CharField(max_length=20, default='white', null=True)
    price_per_item = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создано')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.product.title


class Status(models.Model):
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
