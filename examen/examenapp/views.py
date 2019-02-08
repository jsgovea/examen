from django.shortcuts import render, redirect
from .forms import PlayerForm, TeamModel

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def players(request):
    return render(request, 'players.html')

def add_player(request):
    form = PlayerForm()

    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            player = form.save(commit = False)
            player.save()
            return redirect(players)
    return render(request, 'add_player.html', {
        "form": form
    })

def teams(request):
    return render(request, 'teams.html')

def add_team(request):
    form = TeamForm()

    if rquest.method == "POST":
        form = TeamForm(request.POST)
        
    return render(request, 'add_team.html')
