from django import forms
from .models import Player, Team, Stadium


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("team", "name", "games", "touchdowns", "receptions")

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "city", "wins", "losses", "draws")

class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ("name", "capacity", "city")
