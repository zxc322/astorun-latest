from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import ProductInBasket, Order, ProductInOrder, CollectionOrder, ProductInCollectionOrder, Status
from .tg import telegram_bot_send_order_text
from .mail import send_email


def cart_products_counter(session_key):
    counter = ProductInBasket.objects.filter(session_key=session_key, product__in_stock=True).count()
    print(counter, 'products in cart')
    return {'products_counter': counter}


def get_session_key(request):
    session_key = request.session.session_key
    if not session_key:
        session_key = 123
        session_key = request.session.cycle_key()
    return session_key


def add_to_cart(request):
    data = request.POST
    print(data)
    product_id = data.get('product_id')
    size = data.get('product_size')
    color = data.get('product_color')
    price = data.get('product_price')
    session_key = get_session_key(request)

    # trying to find product in cart
    # if it in cart we are increase quantity by 1

    search = ProductInBasket.objects.filter(session_key=session_key, product_id=product_id, size=size, color=color).count()
    if search:
        product = ProductInBasket.objects.get(
            session_key=session_key, product_id=product_id, size=size, price_per_item=price)
        product.quantity += 1
        product.save()
    else:
        ProductInBasket.objects.create(
            session_key=session_key, product_id=product_id, size=size, price_per_item=price, color=color).save()

    return JsonResponse(cart_products_counter(session_key))


def cart(request):
    session_key = get_session_key(request)
    cart_items = ProductInBasket.objects.filter(session_key=session_key, product__in_stock=True).select_related \
    ('product', 'product__category')
    return render(request, 'order/cart.html', {'cart_items': cart_items})


def make_order2(request):
    data = request.POST
    if request.method == 'POST':
        user = get_session_key(request)
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        customer_phone = data.get('customer_phone')
        order_price = int(data.get('hidden_total'))
        delivery_price = int(data.get('delivery_price'))
        delivery_region = data.get('delivery_region')
        delivery_district = data.get('delivery_district')
        delivery_city = data.get('delivery_city')
        nova_poshta_departament = data.get('nova_poshta')
        comment = data.get('comment')
        order = Order.objects.create(
            user=user,
            order_price=order_price,
            delivery_price=delivery_price,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            delivery_region=delivery_region,
            delivery_district=delivery_district,
            delivery_city=delivery_city,
            nova_poshta_departament=nova_poshta_departament,
            comment=comment,
            status=Status.objects.get(id=1)
        )
        for item in data:
            if item.startswith('product_in_cart'):
                item_id = int(item.split('product_in_cart_')[1])
                try:
                    product_in_cart = ProductInBasket.objects.filter(id=item_id)[0]

                    ProductInOrder.objects.create(order=order,
                                                  product=product_in_cart.product,
                                                  size=product_in_cart.size,
                                                  color=product_in_cart.color,
                                                  quantity=product_in_cart.quantity,
                                                  price_per_item=product_in_cart.price_per_item,
                                                  total_price=product_in_cart.product_total_price
                                                  )
                    product_in_cart.delete()
                except IndexError:
                    return redirect(data.get('url_from'))

        # Code for telegram notification

        telegram_bot_send_order_text(order=order, products=ProductInOrder.objects.filter(order_id=order.id).select_related('product'))
        send_email(order, '{}/order/completed_detail/{}'.format(request.get_host(), order.id))
        redirect_url = data.get('url_from')
        return redirect('{}completed_detail/{}'.format(redirect_url[:-5], order.id))
    return HttpResponse(request.POST)


def change_quantity(request):
    quantity = request.POST.get('quantity')
    pk = request.POST.get('item_id')
    item = ProductInBasket.objects.get(id=pk)
    item.quantity = quantity
    item.save()
    return JsonResponse({})


def remove_item_from_cart(request):
    pk = request.POST.get('item_id')
    ProductInBasket.objects.filter(id=pk).delete()
    # Lets change product counter directly
    return JsonResponse(cart_products_counter(get_session_key(request)))


def completed_orders(request):
    users_orders = reversed(Order.objects.filter(user=get_session_key(request)))
    users_col_orders = reversed(CollectionOrder.objects.filter(user=get_session_key(request)))
    return render(request, 'order/completed.html', {'orders': users_orders, 'col_orders': users_col_orders})


def completed_detail(request, pk):
    order = ProductInOrder.objects.filter(order_id=pk).select_related('product')
    return render(request, 'order/completed_detail.html', {'order': order, 'order_id': pk})


def completed_col_detail(request, pk):
    order = ProductInCollectionOrder.objects.filter(col_order_id=pk).select_related('product')
    return render(request, 'order/completed_detail.html', {'order': order, 'order_id': pk})
