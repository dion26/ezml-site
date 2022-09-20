from django.contrib import admin

from .models import Player, SocialMedia, Position

 
class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('nickname',), }
    list_display = ('pk', 'nickname', 'fullname', 'country', 'role', 'status')
    
    def set(self, obj):
        return obj.set

    set.admin_order_field = 'set__name'
admin.site.register(Player, PlayerAdmin)

admin.site.register(SocialMedia)
admin.site.register(Position)