from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Matches,playerInfo

# Create your views here.

class GameListView(ListView):
    model=Matches
    template_name="freefire/matchlist.html"

class GameDetailView(DetailView):
    model=Matches
    template_name="freefire/matchdetail_list.html"

class PlayerListView(ListView):
    model=playerInfo
    template_name="freefire/playerlist.html"

class PlayerDetailView(DetailView):
    model=playerInfo
    template_name="freefire/player_detail_list.html"


