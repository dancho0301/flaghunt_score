from django.contrib import admin
from .models import Player
from .models import Event
from .models import Team
from .models import TeamMember
from .models import Game

# Register your models here.
admin.site.register(Player)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Game)