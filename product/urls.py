from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # path('', views.Shop.as_view(), name='shop'),
    path('', views.shop, name='shop'),
    path('<slug:slug>/', views.CategoriesItems.as_view(), name='categories'),
    path('<str:gender>/<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),
]
