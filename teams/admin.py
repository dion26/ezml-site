from django.contrib import admin
from .models import Team, Membership

admin.site.register(Team)

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('pk', 'player', 'team', 'date_joined', 'date_left')
    def set(self, obj):
        return obj.set

    set.admin_order_field = 'set__name'
admin.site.register(Membership, MembershipAdmin)