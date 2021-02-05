from django.urls import path
from . import views

urlpatterns = [
    path("", views.GameView.as_view()),
    path("<int:game_id>", views.GameDetailView.as_view(), name='detail'),
]