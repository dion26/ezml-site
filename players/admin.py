from django.contrib import admin

from .models import Player

 
class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('nickname',), }
admin.site.register(Player, PlayerAdmin)