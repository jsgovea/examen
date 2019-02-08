from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def players(request):
    return render(request, 'players.html')

def add_player(request):
    return render(request, 'add_player.html')
