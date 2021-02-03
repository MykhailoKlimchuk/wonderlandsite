from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Game

def index(request):
    games = Game.objects.all()
    print(games)
    return render(request, 'GameArticles/store.html', {'games': games})


def game_detail(request, game_id):
    try:
        game = Game.objects.get(id=game_id)
    except:
        raise Http404("Game not found")

    return render(request, 'GameArticles/game_detail.html', {'game': game})
