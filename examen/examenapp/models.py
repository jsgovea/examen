from django.db import models
from django import forms


# Create your models here.

# POSITION_CHOICES = (
#
# )


class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de equipo")
    city = models.CharField(max_length=50, verbose_name="Ciudad")
    wins = models.IntegerField(verbose_name="Juegos ganados")
    losses = models.IntegerField(verbose_name="Juegos perdidos")
    draws = models.IntegerField(verbose_name="Juegos empatados")

    def __str__(self):
        return self.name


class Player(models.Model):
    team_link = models.ForeignKey('Team', on_delete="CASCADE", null=True)
    team = models.CharField(max_length=100, verbose_name="Equipo", null=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    games = models.IntegerField(verbose_name="Juegos jugados")
    touchdowns = models.IntegerField(verbose_name="Touchdowns")
    receptions = models.IntegerField(verbose_name="Pases completos o recepciones")

    def __str__(self):
        return self.name



# STATUS_CHOICES = (
#
# )
