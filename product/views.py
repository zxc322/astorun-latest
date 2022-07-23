from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from django.views.decorators.cache import cache_page

from product.models import Product, ProductSize, ProductCategory, ProductImage, ProductColor



def shop(request):
    categories = ProductCategory.objects.all()
    return render(request, 'product/shop.html', {'categories': categories})


class Shop(ListView):
    model = ProductCategory
    template_name = 'product/shop.html'
    context_object_name = 'categories'


class CategoriesItems(ListView):
    model = Product
    template_name = 'product/category.html'
    context_object_name = 'products'

    # get all objects with chosen category

    def get_queryset(self, **kwargs):
        global cat_slug
        cat_slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=cat_slug, in_stock=True).select_related('category')

    # get chosen category name for title of page

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = ProductCategory.objects.get(slug=cat_slug)
        context['cat_name'] = cat.category
        return context


def product_detail(request, gender, cat_slug, prod_slug):

    # Get all products with chosen gender and category
    products = Product.objects.filter(category__slug=cat_slug, gender=gender, in_stock=True)

    # And get chosen product by slug
    current_obj = get_object_or_404(Product, slug=prod_slug)

    # Get all sizes for this product
    size = ProductSize.objects.filter(product__slug=prod_slug)

    # Now we splitting QuerySet to place 1 object on 1 page

    paginator = Paginator(products, 1)
    if current_obj in products:
        current_page = list(products).index(current_obj) + 1
    else:
        response = render(request, 'mainFront/page404.html')
        response.status_code = 404
        return response
    page_obj = paginator.get_page(current_page)
    if page_obj.has_previous():
        prev_slug = (products[current_page-2]).slug
    else:
        prev_slug = None
    if page_obj.has_next():
        next_slug = (products[current_page]).slug
    else:
        next_slug = None

    # Get all images ans colors of current object

    images = ProductImage.objects.filter(product__slug=prod_slug)
    colors = ProductColor.objects.filter(product__slug=prod_slug)
    return render(request, 'product/product_detail.html',
                  {'page_obj': page_obj,
                   'prev_slug': prev_slug,
                   'gender': gender,
                   'cat_slug': cat_slug,
                   'next_slug': next_slug,
                   'size': size,
                   'colors': colors,
                   'images': images})


