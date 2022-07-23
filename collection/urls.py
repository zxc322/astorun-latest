from django.urls import path
from . import views

app_name = 'collection'
urlpatterns = [
    path('', views.Collections.as_view(), name='collection'),
    path('buy_collection', views.buy_collection, name='buy_collection'),
    path('<slug:slug>/<str:gender>/', views.SliderCollection.as_view(), name='slider_collection'),
    path('make_col_order/', views.make_col_order, name='make_col_order'),
]
