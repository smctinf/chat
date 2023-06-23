from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    # <str:room_name> is affirmating that the parameter room_name need to be string.
    path('<str:room_name>/', views.room, name='room'),
]
    