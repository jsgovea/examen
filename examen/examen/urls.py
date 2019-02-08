from django.contrib import admin
from django.urls import path
from examenapp import views
from django.contrib.auth import views as auth_views


#Password administrador123

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    # path('NFLP/iniciar-sesion/$', auth_views.login,
    # {'template_name': 'nflp/sign_in', name="nflp-sign-in"}),
    path('NFLP/jugadores/', views.players, name="players"),
    path('NFLP/jugadores/agregar/', views.add_player, name="add-player"),

]
