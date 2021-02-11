from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("projects/", views.GameView.as_view(), name="projects"),
    path("gallery/", views.GalleryView.as_view(), name="gallery"),
    path("our_team/", views.TeamView.as_view(), name="our_team"),
    path("contact_us/", views.ContactUsView.as_view(), name="contact_us"),
    path("contact_us/", views.ContactUsView.as_view(), name="contact_us"),
    path("projects/<int:game_id>/", views.GameDetailView.as_view(), name='detail'),
]