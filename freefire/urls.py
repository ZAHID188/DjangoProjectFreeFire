from django.urls import path
from .views import GameListView,PlayerListView,GameDetailView,PlayerDetailView

urlpatterns=[
    path("" ,GameListView.as_view(),name="game-list"),
    path("games/<int:pk>/",GameDetailView.as_view(),name="game-detail"),
    path("players" ,PlayerListView.as_view(),name="player-list"),
    path("players/<int:pk>" ,PlayerDetailView.as_view(),name="player-detail"),
    

]