from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Artist, Album
from .forms import ArtistForm, AlbumForm

def index(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    context = {
        'artists': artists,
        'albums': albums
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
    
def artists(request, artist_id):
    artist = Artist.objects.get(pk=artist_id) 
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist 
    }
    return HttpResponse(template.render(context, request))

def albums(request, album_id):
    album = Album.objects.get(pk=album_id)  
    template = loader.get_template('display_album.html')
    context = {
        'album': album  
    }
    return HttpResponse(template.render(context, request))


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Agregar paréntesis
            return redirect('album_manager:index')
    else:
        form = ArtistForm()
    return render(request, 'artist_form.html', {'form': form})

def edit_artist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)  
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()  
            return redirect('album_manager:index')  
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist_form.html', {'form': form})
    
def delete_artist(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    artist.delete()  
    return redirect('album_manager:index')

################### Vistas de Album #####################

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    return render(request, 'album_form.html', {'form': form})

def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id) 
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')   
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})

def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    return redirect('album_manager:index')