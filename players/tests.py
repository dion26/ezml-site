from django.test import TestCase
from players.models import Player, Position
from teams.models import Team, Membership
# Create your tests here.

class PlayerTeamTest(TestCase):
    def setUp(self):
        all_position = Position.objects.all()
        number_of_team = 2
        for team in range(number_of_team):
            current_team = Team.objects.create(name=f'team{team}')
            for pos in all_position:
                current_player = Player.objects.create(nickname=f"player_{pos.name}_{team}")
                Membership.objects.create(team=current_team, player=current_player)

    def test_player_in_team(self):
        player = Player.objects.get(nickname="player_Jungler_0")
        team0 = Team.objects.get(name="team0")
        team1 = Team.objects.get(name="team1")

        self.assertEqual(player.team_set.first(), team0)
        self.assertNotEqual(player.team_set.first(), team1)
