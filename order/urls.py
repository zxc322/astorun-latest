from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('make_order/', views.make_order2, name='make_order'),
    path('completed_orders/', views.completed_orders, name='completed_orders'),
    path('completed_detail/<int:pk>/', views.completed_detail, name='completed_detail'),
    path('completed_col_detail/<int:pk>/', views.completed_col_detail, name='completed_col_detail'),
    path('change_quantity/', views.change_quantity, name='change_quantity'),
    path('remove_item_from_cart/', views.remove_item_from_cart, name='remove_item_from_cart'),
    ]
