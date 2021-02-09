from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Game


class GameView(View):
    def get(self, request):
        games = Game.objects.all()

        return render(request, "games/games_list.html", {"games_list": games})


class GameDetailView(View):
    def get(self, request, game_id):
        game = Game.objects.get(id=game_id)
        reviews = game.review_set.all()
        return render(request, "games/game_detail.html", {"game": game, "reviews": reviews})


class HomeView(View):
    def get(self, request):
        return render(request, "games/home.html", {})
