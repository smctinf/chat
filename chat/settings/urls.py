from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include('authentication.urls'), name='authentication'),
    path('chat/', include('chat.urls'), name="chat"),
    path('admin/', admin.site.urls, name="admin"),
]