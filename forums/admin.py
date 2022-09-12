from django.contrib import admin

from .models import Thread, Comment, Subforum, LikeThread, DisLikeThread

class ThreadAdmin(admin.ModelAdmin):
    list_display= ('name', 'get_total_likes', 'get_total_dis_likes',)

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Subforum)
admin.site.register(Comment)

class LikeThreadAdmin(admin.ModelAdmin):
    fields=('users',)
    list_display= ('thread', 'get_total_likes',)

admin.site.register(LikeThread, LikeThreadAdmin)

class DisLikeThreadAdmin(admin.ModelAdmin):
    fields=('users',)
    list_display= ('thread', 'get_total_dis_likes',)

admin.site.register(DisLikeThread, DisLikeThreadAdmin)

