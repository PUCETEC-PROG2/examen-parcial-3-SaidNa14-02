from django import forms
from .models import Album, Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'country']
        labels = {
            'name': 'Nombre',
            'country': 'País',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'gender', 'artist', 'cover']
        labels = {
            'title': 'Título',
            'release_year': 'Año de lanzamiento',
            'gender': 'Género',
            'artist': 'Artista',
            'cover': 'Portada',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
        }