from django.db import models

class Room(models.Model):
    name = models.CharField(blank=False,unique=True,max_length=100, verbose_name="Name of room")
    display_name = models.CharField(blank=False, unique=True, max_length=100, verbose_name="Name that will be display")
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Owner of the room")
    date_of_creation = models.DateField(auto_now=True, verbose_name="Date of creation")

    def __str__(self):
        return self.name
