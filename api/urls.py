from django.urls import path
from . import views

urlpatterns = [
    path('artist/', views.get_artist_list, name='artist'),
    path('album/', views.get_albums_tracks_list, name='album'),
    path('album/artist/<int:artist_id>/', views.get_albums_artist_list, name='album-artist'),
    path('track/album/<int:album_id>/', views.get_tracks_album_list, name='track-album'),
    path('album/info/', views.get_info_album_list, name='album-info'),
]