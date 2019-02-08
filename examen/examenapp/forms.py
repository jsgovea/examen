from django import forms

from .models import Player, Team


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("team", "name", "games", "touchdowns", "receptions")

class TeamModel(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "city", "wins", "losses", "draws")
