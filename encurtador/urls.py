from django.urls import path
from . import views

#app_name="encurtador"

urlpatterns = [
    path('encurtadordelink', views.encurtadordelink, name="encurtadordelink"),
]
