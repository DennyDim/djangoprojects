from django.shortcuts import render, redirect

from album.models import Album
from user.models import Profile
from user.forms import ProfileForm


def get_profile():
    return Profile.objects.first()


def main_page(request):
    profile = get_profile()
    form = ProfileForm(request.POST or None)

    if profile:
        context = {
            'profile': profile,
            'albums': Album.objects.all(),
        }
        return render (request, 'home_page.html', context)
    else:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                albums = Album.objects.all()
                context = {'albums': albums,
                       "profile": profile, }
                return render(request, 'home_page.html', context)

        context = {
            "form": form,
            }
        return render(request, 'profile/register_page.html', context)


def profile_details(request):
    profile = get_profile()
    albums_legnth = len(Album.objects.all())

    context = {
        'profile': profile,
        'albums_legnth':albums_legnth,
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        return redirect('main page')

    context = {
        'profile': profile
    }
    return render(request, 'profile/profile-delete.html', context)