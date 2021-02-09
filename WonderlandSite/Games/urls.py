from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("projects/", views.GameView.as_view(), name="projects"),
    path("projects/<int:game_id>/", views.GameDetailView.as_view(), name='detail'),
]