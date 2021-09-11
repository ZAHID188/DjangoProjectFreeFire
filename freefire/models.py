from django.db import models
import uuid,time
#from django.utils.translation import activate

# Create your models here.

mapchoice=(("BERMUDA","KALAHARI"),("BERMUDA","BERMUDA"))
gamechoice=(("CLASH_SQUAD","CLASH SQUAD"),("CLASSIC","CLASSIC"))
ammuchoice=(("limited","LIMITED"),("unlimited","UNLIMITED"))
gametime=(("10am","10AM"),("2am","2AM"))
entryfeechoice=((15.0,15),(50.0,50),(100.0,100.0))


UUID=uuid.uuid1(node=None,clock_seq=None)

class Matches(models.Model):
    #gameid =models.UUIDField(default=str(uuid.uuid4), editable=False)
    #gameid=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    
    Matchid=models.CharField(max_length=100, blank=True, unique=True, default=UUID.time)
    GameMood=models.CharField(max_length=120,choices=gamechoice,default="CLASSIC")
    map=models.CharField(max_length=50,choices=mapchoice,default="BERMUDA")
    ammu=models.CharField(max_length=20, choices=ammuchoice ,default="Limited")
    time=models.CharField(max_length=20, choices=gametime ,default="00PM")
    entryfee=models.FloatField(choices=entryfeechoice,default=15.0)
    matchnumber=models.IntegerField()
    
    
   

    def __str__(self):
         return self.GameMood + " "+ self.Matchid





class playerInfo(models.Model):
    player_name=models.CharField(max_length=120)
    user_id=models.IntegerField()
    Profile_picture=models.ImageField(blank=True,null=True)
    password=models.CharField(max_length=20)


    def __str__(self):
        return self.player_name 


