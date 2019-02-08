from django.contrib import admin
from django.urls import path
from examenapp import views


#Password administrador123

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home")
]
