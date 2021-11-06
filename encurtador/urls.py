from django.urls import path
from . import views

app_name="encurtador"

urlpatterns = [
    path('', views.encurtar, name="encurtadordelink"),
]
