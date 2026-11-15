from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("programok/", views.programok, name="programok"),
    path("velemenyek/", views.velemenyek, name="velemenyek"),
    path("kapcsolat/", views.kapcsolat, name="kapcsolat"),
]
