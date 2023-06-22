from django.contrib.auth.models import User
from django.shortcuts import render

def lobby(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    context = {
        "room_name" : room_name, 
    }
    return render(request, 'chat/room.html', context)   