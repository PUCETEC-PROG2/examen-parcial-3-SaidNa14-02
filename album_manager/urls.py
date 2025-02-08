# Ingresar tus URLs de la app aquí

from django.urls import path
from . import views

app_name = 'album_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_album/', views.add_album, name='add_album'),
    path('artist/<int:artist_id>/', views.artists, name='display_artist'),
    path('album/<int:album_id>/', views.albums, name='display_album'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
]