from django.contrib import admin
from .models import Player, Match, Team, News

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(News)

# Register your models here.
