from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=5, decimal_places=2)


class User(models.Model):  #
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    passport = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)
    is_admin = models.BooleanField(default=False)
    discount = models.ManyToManyField(Discount)


class Room(models.Model):  #
    number = models.IntegerField()
    capacity = models.IntegerField(default=2)
    comfort = models.CharField(max_length=20, default="standard")
    price = models.IntegerField(default=100)
    is_free = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)


class Settlement(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True)


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
    price = models.DecimalField(max_digits=10, decimal_places=2)
