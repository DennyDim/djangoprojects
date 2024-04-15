
from django.urls import path, include
from album import views

urlpatterns = [
        path('add/', views.add_album, name='add album'),

        path('<int:album_id>/', include([
                path('details/', views.album_details, name='album details'),
                path('edit/', views.UpdateAlbumView.as_view(), name='edit album'),
                path('delete/', views.delete_album, name='delete album'),
        ]))
]