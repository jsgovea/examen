from django.contrib import admin
from django.urls import path
from examenapp import views
from django.contrib.auth import views as auth_views

# User admin
# Password administrador123

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('NFLP/iniciar-sesion/$', auth_views.login,
    # {'template_name': 'nflp/sign_in', name="nflp-sign-in"}),
    path('NFLP/jugadores/', views.players, name="players"),
    path('NFLP/jugadores/agregar/', views.add_player, name="add-player"),
    path('NFLP/equipos/', views.teams, name="teams"),
    path('NFLP/equipos/agregar', views.add_team, name="add-team"),
    path('NFLP/estadios/', views.stadiums, name="stadiums"),
    path('NFLP/estadios/agregar', views.add_stadium, name="add-stadium")


]
