from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return str(self.room)
