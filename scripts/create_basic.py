from product.models import ProductCategory
from order.models import Status
from mainFront.models import Documentation

def run():
    ProductCategory.objects.create(category='Hats', slug='hats')
    ProductCategory.objects.create(category='Jewellery', slug='jewellery')
    ProductCategory.objects.create(category='Shirts', slug='shirts')
    ProductCategory.objects.create(category='T-shirts', slug='tshirts')
    ProductCategory.objects.create(category='Sweatshirts', slug='sweatshirts')
    ProductCategory.objects.create(category='Underwear', slug='underwear')
    ProductCategory.objects.create(category='Outerwear', slug='outerwear')   
    ProductCategory.objects.create(category='Accessories', slug='accessories')
    ProductCategory.objects.create(category='Trousers', slug='trousers')
    ProductCategory.objects.create(category='Shorts', slug='shorts')
    ProductCategory.objects.create(category='Socks', slug='socks')
    ProductCategory.objects.create(category='Footwear', slug='footwear')
    ProductCategory.objects.create(category='Home & Pyjamas', slug='home_and_pyjamas')
    ProductCategory.objects.create(category='Sportswear', slug='sportswear')
    ProductCategory.objects.create(category='For Work', slug='for_work')
    ProductCategory.objects.create(category='For Hobbies', slug='for_hobbies')
    ProductCategory.objects.create(category="Children's", slug='childrens')
    ProductCategory.objects.create(category='Interesting', slug='interesting')
    ProductCategory.objects.create(category='Costumes', slug='costumes')

    print('Categories created')

    Status.objects.create(status='waiting for payment confirmation')
    Status.objects.create(status='preparing for ship')
    Status.objects.create(status='order on the way')
    Status.objects.create(status='order successfully delivered')

    print('statuses created')

    Documentation.objects.create(title='FAQ', slug='faq', text='empty')
    Documentation.objects.create(title='RULES', slug='rules', text='empty')
    Documentation.objects.create(title='OFFER', slug='offer', text='empty')
    Documentation.objects.create(title='DELIVERY', slug='delivery', text='empty')
    Documentation.objects.create(title='ABOUT US', slug='about_us', text='empty')

    print('footer created')