from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.MyNews.as_view(), name='news'),
    path('<slug:slug>/', views.load_news, name='load_news'),
]
