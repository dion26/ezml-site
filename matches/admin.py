from django.contrib import admin
from .models import Series, Tournament, Participation, Match
# Register your models here.
admin.site.register(Series)
admin.site.register(Tournament)
admin.site.register(Participation)
admin.site.register(Match)