from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Artists
from .models import Albums
from .models import Tracks


# Create your views here.

@api_view(['GET'])
def get_artist_list(request):

    artists = Artists.objects.all().values('Name', 'ArtistId')
    list_artists = [{"Name": artist["Name"], "ArtistId": artist["ArtistId"]} for artist in artists]

    return Response(list_artists)


@api_view(['GET'])
def get_albums_tracks_list(request):
    list_dict_albums_tracks = []
    for album in Albums.objects.values('AlbumId', 'Title'):
        tracks = Tracks.objects.filter(AlbumId=album["AlbumId"]).values('Name')
        dict_album_track = {"Title": album["Title"], "AlbumId": album["AlbumId"], "Tracks": [track["Name"] for track in tracks]} 
        list_dict_albums_tracks.append(dict_album_track)

    return Response(list_dict_albums_tracks)


@api_view(['GET'])
def get_albums_artist_list(request, artist_id):
    albums_artist = Albums.objects.filter(ArtistId=artist_id).values('Title')
    list_albums_artist = [album["Title"] for album in albums_artist]
    return Response(list_albums_artist)


@api_view(['GET'])
def get_tracks_album_list(request, album_id):
    tracks_album = Tracks.objects.filter(AlbumId=album_id).values('Name')
    list_tracks_album = [track["Name"] for track in tracks_album]
    return Response(list_tracks_album)


@api_view(['GET'])
def get_info_album_list(request):
    list_dict_albums_info = []
    for album in Albums.objects.values('AlbumId', 'Title', 'ArtistId'):
        tracks = Tracks.objects.filter(AlbumId=album["AlbumId"]).count()
        artist = Artists.objects.filter(ArtistId=album["ArtistId"]).values('Name')
        dict_album_track = {"Album": album["Title"], "Tracks": tracks, "Artist": artist[0]["Name"]} 
        list_dict_albums_info.append(dict_album_track)

    return Response(list_dict_albums_info)