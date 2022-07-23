from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('get_form/', views.get_form, name='get_form'),
]
