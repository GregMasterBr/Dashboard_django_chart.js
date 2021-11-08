from django.urls import path
from . import views

app_name="encurtador"

urlpatterns = [
    path('', views.encurtar, name="encurtar"),
    path('valida_link/', views.valida_link, name="valida_link"),
    path('/<str:link>/', views.redirecionar, name="redirecionar"),

]

