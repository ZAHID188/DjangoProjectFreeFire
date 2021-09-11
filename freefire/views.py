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



            # Let's create API


from django.http import JsonResponse, request,response


def matchlistapi(request):
    matches=Matches.objects.all()
    data={"matches are ":list(matches.values())}
    response=JsonResponse(data)
    return response

def matchdetailsapi(request,pk):
    try:
        matchdetail=Matches.objects.get(pk=pk)
        data={"match detail":{
            "match Id":matchdetail.Matchid,
            "match mood":matchdetail.GameMood,

        }}
        response=JsonResponse(data)
    except Matches.DoesNotExist:
        response=JsonResponse({"error":{"data is not valid":404}},status=404)
    
    return response


def playerlistapi(request):
    playerlist=playerInfo.objects.all()
    data={ "Player List":list(playerlist.values())}
    response=JsonResponse(data)
    
    return response
    

def playerdetailsapi(request,pk):
    try:
        playerdetail=playerInfo.objects.get(pk=pk)
        data={"Player Details":{
            "player name":playerdetail.player_name,
            "player id":playerdetail.user_id,
            "player pic":playerdetail.Profile_picture.url,
            "player pass":playerdetail.password,

            
        }}
        response=JsonResponse(data)
        

    except playerInfo.DoesNotExist:
        response=JsonResponse({"problem":{
            "error":404,
            "error details":"no data"
        }},status=404)
    return response





