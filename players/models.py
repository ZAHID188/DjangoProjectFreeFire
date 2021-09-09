from django.db import models
#from django.utils.translation import activate

# Create your models here.

mapchoice=(("BERMUDA","KALAHARI"),("BERMUDA","BERMUDA"))
gamechoice=(("CLASH_SQUAD","CLASH SQUAD"),("CLASSIC","CLASSIC"))
ammuchoice=(("limited","LIMITED"),("unlimited","UNLIMITED"))
gametime=(("10am","10AM"),("2am","2AM"))

class Matches(models.Model):
    GameMood=models.CharField(max_length=120,choices=gamechoice,default="CLASSIC")
    map=models.CharField(max_length=50,choices=mapchoice,default="BERMUDA")
    ammu=models.CharField(max_length=20, choices=ammuchoice ,default="Limited")
    time=models.CharField(max_length=20, choices=gametime ,default="00PM")
   

    def __str__(self):
         return self.GameMood





class playerInfo(models.Model):
    player_name=models.CharField(max_length=120)
    game_id=models.IntegerField()

    def __str__(self):
        return self.player_name


