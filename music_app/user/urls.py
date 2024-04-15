
from django.urls import path, include

from user import views

urlpatterns = [
    path("", views.main_page, name="main page"),

    path('profile/', include([
        path('details/', views.profile_details, name='profile details'),
        path('delete/', views.delete_profile, name='delete profile'),
    ]))

]