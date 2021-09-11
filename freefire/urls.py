from django.urls import path
from .views import (GameListView,PlayerListView,GameDetailView,PlayerDetailView, 
                     matchlistapi,matchdetailsapi,playerlistapi,playerdetailsapi)

urlpatterns=[
    path("" ,GameListView.as_view(),name="game-list"),
    path("games/<int:pk>/",GameDetailView.as_view(),name="game-detail"),
    path("players" ,PlayerListView.as_view(),name="player-list"),
    path("players/<int:pk>" ,PlayerDetailView.as_view(),name="player-detail"),
    path("api/matches/" ,matchlistapi,name="match-list"),
    path("api/matches/<int:pk>" ,matchdetailsapi,name="match-detail"),
    path("api/players/" ,playerlistapi,name="player-list"),
    path("api/players/<int:pk>" ,playerdetailsapi,name="player-detail"),

    #api urls

        

]