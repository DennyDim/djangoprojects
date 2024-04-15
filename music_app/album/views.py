from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from album.forms import AlbumForm
from album.models import Album

from user.models import Profile


def add_album(request):
    profile = Profile.objects.first()
    albums = Album.objects.all()
    form = AlbumForm(request.POST or None)

    if request.method == "POST":
        form.instance.owner = profile
        if form.is_valid():
            form.save()
            return redirect('main page')

    context = {
        "form": form,
        "profile": profile,
        "albums":  albums
    }
    return render(request, "albums/album-add.html", context)


def album_details(request, album_id: int):
    album = Album.objects.get(pk=album_id)

    context = {
        "current_album": album
    }
    return render(request, "albums/album-details.html", context)


class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "albums/album-edit.html"
    success_url = reverse_lazy('main page')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('album_id')
        return get_object_or_404(Album, pk=pk)



def delete_album(request, album_id):

    album = Album.objects.get(id=album_id)
    form = AlbumForm(instance=album)

    for field in form.fields.values():
        field.widget.attrs['readonly'] = True

    if request.method == "POST":

        album.delete()
        return redirect('main page')

    context = {
        "album": album,
        "form": form
    }

    return render(request, "albums/album-delete.html", context)