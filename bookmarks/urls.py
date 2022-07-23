from django.urls import path
from . import views

app_name = 'bookmarks'
urlpatterns = [
    path('', views.bookmarks, name='bookmarks'),
    path('add/', views.add_to_bookmarks, name='add_to_bookmarks'),
    path('remove/', views.remove_from_bookmarks, name='remove_from_bookmarks'),
    path('delete/', views.remove_bookmarks, name='remove_bookmarks'),
    path('api/', views.bookmarks_api, name='bookmarks_api'),
]