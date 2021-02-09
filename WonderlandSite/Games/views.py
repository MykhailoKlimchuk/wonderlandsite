from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import Game
from .models import Teammate


class GameView(View):
    def get(self, request):
        games = Game.objects.all()
        games_list = []
        i = 0
        j = 3
        while True:
            games_list.append(games[i:j])
            i += 3
            j += 3
            if j == len(games):
                break
            if j > len(games):
                games_list.append(games[i:len(games)])
            break

        return render(request, "games/games_list.html", {"games_list": games_list})


class GameDetailView(View):
    def get(self, request, game_id):
        game = Game.objects.get(id=game_id)
        reviews = game.review_set.all()
        return render(request, "games/game_detail.html", {"game": game, "reviews": reviews})


class HomeView(View):
    def get(self, request):
        return render(request, "home.html", {})


class TeamView(View):
    def get(self, request):
        teammates = Teammate.objects.all()
        print(teammates)
        teammates_list = []
        i = 0
        j = 3
        while True:
            teammates_list.append(teammates[i:j])
            i += 3
            j += 3
            if j == len(teammates):
                break
            if j > len(teammates):
                teammates_list.append(teammates[i:len(teammates)])
            break
        print(teammates_list)
        return render(request, "team.html", {"teammates_list": teammates_list})
