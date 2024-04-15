
from django import forms
from album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']

        widgets = {
            'album_name': forms.TextInput(
                attrs={'placeholder': "Album Name"}
            ),
            'email': forms.EmailInput(
                attrs={'artist': "Artist"}
            ),
            "description": forms.Textarea(
                attrs={'placeholder': "Description"}
            ),
            "image_url": forms.TextInput(
                attrs={'placeholder': "Image URL"}
            ),
            "price": forms.TextInput(
                attrs={'placeholder': "Price"}
            ),
        }
