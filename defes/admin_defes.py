import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation, Discount, User, Settlement
from defes import general_defes


def create_settlement(user, number, in_data, out_data):
    room = Room.objects.get(number=number)
    settlement = Settlement.objects.create(
        user=user,
        room=room,
        check_in_date=in_data,
        check_out_date=out_data
    )
    settlement.save()


def get_user_by_passport(passport):
    try:
        return User.objects.get(passport=passport)
    except Exception as e:
        print(e)


def delete_user_disc(user, discount_name):
    try:
        discount = Discount.objects.get(name=discount_name)
        user.discount.remove(discount)
        user.save()
    except Exception as e:
        print(e)


def add_discount_to_user(user, discount_name):
    try:
        discount = Discount.objects.get(name=discount_name)
        user.discount.add(discount)
        user.save()
    except Exception as e:
        print(e)
