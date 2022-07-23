from django.shortcuts import render, redirect, get_object_or_404

from .local_url_generator import local_url_generator
from .models import Collection
from product.models import Product, ProductSize, ProductColor
from order.models import CollectionOrder, ProductInCollectionOrder, Status
from django.views.generic import ListView
from order.views import get_session_key
from order.tg import telegram_bot_send_col_order_text
from order.mail import send_email
import os

host = os.environ.get('HOSTNAME')


class Collections(ListView):
    paginate_by = 9
    model = Collection
    template_name = 'collection/collection.html'
    context_object_name = 'collections'

    def get_queryset(self, **kwargs):
        return Collection.objects.filter(is_active=True)


class SliderCollection(ListView):
    model = Product
    template_name = 'collection/slider_collection.html'
    context_object_name = 'parsed_collection'

    def get_queryset(self, **kwargs):
        global slug
        global gender
        slug = self.kwargs['slug']
        gender = self.kwargs['gender']
        return Product.objects.filter(collection__slug=slug, gender=gender, in_stock=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        col = Collection.objects.get(slug=slug)
        context['col_name'] = col.collection_name

        sizes = ProductSize.objects.filter(product__collection__slug=slug, product__gender=gender)
        colors = ProductColor.objects.filter(product__collection__slug=slug, product__gender=gender)
        context['sizes'] = sizes
        context['colors'] = colors
        context['gender'] = gender
        return context


def buy_collection(request):
    if request.method == 'POST':
        data = request.POST
        url_from = data.get('url_from')
        order_price = int(data.get('discount-price'))
        discount = data.get('discount-percent')
        ids = data.get('discount-ids')
        gender = data.get('gender')
        sizes = data.getlist('chosen-size')
        colors = data.getlist('chosen-color')
        print('sizes: ', sizes)
        print('ids: ', ids)
        item_dicts = []
        sizes_list = list()
        colors_list = list()
        split_ids = ids.split(',')
        first_id = int(split_ids[0])
        collection_name = Product.objects.get(id=first_id).collection.collection_name
        order_list = list()
        print('ids:', ids.split(','))
        for item in ids.split(','):
            n_dict = dict()
            order_string = '-'
            qs = Product.objects.filter(id=int(item)).select_related('category')

            n_dict['id'] = int(item)
            order_string += item + '-'
            for prod in qs:
                n_dict['category'] = prod.category.category
                n_dict['category_slug'] = prod.category.slug
                n_dict['title'] = prod.title
                n_dict['slug'] = prod.slug
                n_dict['image'] = prod.main_image.url
                n_dict['item_price'] = prod.price



            for size in sizes:
                parsed = size.split('=')
                if parsed[0] == item:
                    if parsed[1]:
                        n_dict['size'] = parsed[1]
                        break
                    else:
                        n_dict['size'] = 'UniSize'
                        break

            for color in colors:
                parsed = color.split('=')
                if parsed[0] == item:
                    if parsed[1]:
                        n_dict['color'] = parsed[1]
                        break
                    else:
                        n_dict['color'] = '***'
                        break
            item_dicts.append(n_dict)
            order_list.append(order_string)

        for i in ids.split(','):
            for size in sizes:
                parsed = size.split('=')
                if parsed[0] == i:
                    if parsed[1]:
                        sizes_list.append(parsed[1])
                    else:
                        sizes_list.append('UniSize')

        for i in ids.split(','):
            for color in colors:
                parsed = color.split('=')
                if parsed[0] == i:
                    if parsed[1]:
                        colors_list.append(parsed[1])
                    else:
                        colors_list.append('***')

        order_sizes = ','.join(sizes_list)
        order_colors = ','.join(colors_list)

        return render(request, 'collection/buy_collection.html', {'set': item_dicts,
                                                                  'collection_name': collection_name,
                                                                  'order_price': order_price,
                                                                  'discount': discount,
                                                                  'gender': gender,
                                                                  'order_list': order_list,
                                                                  'order_sizes': order_sizes,
                                                                  'order_colors': order_colors,
                                                                  'ids': ids,
                                                                  'url_from': url_from,
                                                                  })
    else:
        return render(request, 'mainFront/page404.html')


def make_col_order(request):
    data = request.POST
    if request.method == 'POST':
        user = get_session_key(request)
        customer_name = data.get('customer_name')
        customer_email = data.get('customer_email')
        customer_phone = data.get('customer_phone')
        order_price = int(data.get('order-price'))
        discount_percent = data.get('discount-percent')
        delivery_region = data.get('delivery_region')
        delivery_district = data.get('delivery_district')
        delivery_city = data.get('delivery_city')
        nova_poshta_departament = data.get('nova_poshta')
        comment = data.get('comment')

        col_order = CollectionOrder.objects.create(
            user=user,
            order_price=order_price,
            discount_percent=discount_percent,
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

        ids = data.get('ids').split(',')
        sizes = data.get('sizes').split(',')
        colors = data.get('colors').split(',')

        for i in range(len(ids)):
            product = get_object_or_404(Product, id=int(ids[i]))

            ProductInCollectionOrder.objects.create(col_order=col_order,
                                                    product=product,
                                                    size=sizes[i],
                                                    color=colors[i],
                                                    price_per_item=product.price)

        url_from = data.get('url_from')
        print(telegram_bot_send_col_order_text(order=col_order,
                                         products=ProductInCollectionOrder.objects.filter
                                         (col_order_id=col_order.id).select_related('product')))
        send_email(col_order, '{}/order/completed_col_detail/{}'.format(request.get_host(), col_order.id))

        return redirect(
            '{}order/completed_col_detail/{}'.format(local_url_generator(url=data.get('url_from')), col_order.id))
