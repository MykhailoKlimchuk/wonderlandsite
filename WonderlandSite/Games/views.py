from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from .models import Game
from .models import Teammate
from .models import GalleryPhoto
from .forms import ContactUsForm


class GameView(View):
    def get(self, request):
        #     todo зробити через штмл адаптивну таблицю
        games_list = Game.objects.all()

        return render(request, "games/games_list.html", {"games_list": games_list})


class GalleryView(View):
    def get(self, request):
        #     todo зробити через штмл адаптивну таблицю
        gallery_photos = GalleryPhoto.objects.all()

        return render(request, "gallery.html", {"gallery_photos": gallery_photos})


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
        #     todo зробити через штмл адаптивну таблицю
        teammates_list = Teammate.objects.all()
        return render(request, "team.html", {"teammates_list": teammates_list})


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, "contact_us.html", {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        error = ""
        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            error = "form is not valid"

        data = {
            "form": form,
            "error": error,
        }

        return render(request, "contact_us.html", data)

