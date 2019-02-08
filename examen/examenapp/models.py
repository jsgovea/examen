from django.db import models
from django import forms


# Create your models here.

# POSITION_CHOICES = (
#
# )

class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    games = models.IntegerField(verbose_name="Juegos jugados")
    touchdowns = models.IntegerField(verbose_name="Touchdowns")
    receptions = models.IntegerField(verbose_name="Pases completos o recepciones")
    team = models.CharField(max_length=100, verbose_name="Equipo")

    def __str__(self):
        return self.name

# STATUS_CHOICES = (
#
# )
