from django.urls import path
from . import views

app_name = 'mainFront'
urlpatterns = [
    path('', views.main, name='main'),
    path('scroll', views.scroll, name='scroll'),
    path('FAQ', views.FAQ, name='FAQ'),
    path('RULES', views.RULES, name='RULES'),
    path('OFFER', views.OFFER, name='OFFER'),
    path('DELIVERY', views.DELIVERY, name='DELIVERY'),
]