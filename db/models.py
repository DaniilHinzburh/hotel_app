from django.db import models


class User(models.Model):  #
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    password = models.CharField(max_length=255)
    passport = models.IntegerField()
    address = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False)


class Room(models.Model):  #
    number = models.IntegerField()
    capacity = models.IntegerField(default=2)
    comfort = models.CharField(max_length=20, default="standard")
    price = models.IntegerField(default=100)
    is_free = models.BooleanField(default=True)


class Settlement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.IntegerField()
