from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=100)
    Place = models.TextField()
    Phone = models.IntegerField()
    Email = models.EmailField()
    Username = models.CharField(max_length=78)
    Password = models.CharField(max_length=89)

class Booking(models.Model):
    Name = models.CharField(max_length=78)
    Place = models.CharField(max_length=78)
    Phone = models.IntegerField()
    Game = models.CharField(max_length=98)
    Date_Time = models.DateTimeField()

