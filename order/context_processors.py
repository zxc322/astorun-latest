from .models import ProductInBasket


def items_in_cart(request):
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()
    products_counter = ProductInBasket.objects.filter(session_key=session_key, product__in_stock=True).count()
    return locals()
