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
        return render(request, "games/games_detail.html", {"game": game})

