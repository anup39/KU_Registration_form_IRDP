from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path("completed/" ,views.completed,name="completed")
]