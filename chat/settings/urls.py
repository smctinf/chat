from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('chat.urls'), name="chat"),
    path('admin/', admin.site.urls, name="admin"),
]
