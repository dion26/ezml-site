from django.views.generic.base import TemplateView


class MatchesView(TemplateView):
    template_name = 'matches/matches.html'
