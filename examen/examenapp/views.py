from django.shortcuts import render, redirect
from .forms import PlayerForm, TeamForm, StadiumForm
from .models import Player, Stadium, Team

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def players(request):
    context = {
    "player_list": Player.objects.all()
    }
    return render(request, 'players.html', context)

# Agregar jugadores
def add_player(request):
    form = PlayerForm()

    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit = False)
            player.save()
            return redirect(home)
    return render(request, 'add_player.html', {
        "form": form
    })

def teams(request):
    context = {
    "teams_list": Team.objects.all()
    }
    return render(request, 'teams.html', context)

def add_team(request):
    form = TeamForm()

    if request.method == "POST":
        form = TeamForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)
            team.save()
        return redirect(home)
    return render(request, 'add_team.html', {
        "form": form
    })


def stadiums(request):
    context = {
    "stadium_list": Stadium.objects.all()
    }
    return render(request, 'stadium.html', context)

def add_stadium(request):
    form = StadiumForm()

    if request.method == "POST":
        form = StadiumForm(request.POST)

        if form.is_valid():
            stadium = form.save(commit=False)
            stadium.save()
        return redirect(home)
    return render(request, 'add_stadium.html', {
    "form": form
    })
