import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation
from defes.general_defes import count_total_price, apply_discounts


def find_available_rooms(comfort, capacity, num_of_days=None, in_data=None, out_data=None):
    if in_data is None:
        in_data = datetime.now().date()

    if out_data is None and num_of_days is not None:
        out_data = in_data + timedelta(days=num_of_days)

    available_rooms = Room.objects.filter(comfort=comfort, capacity=capacity)

    for room in available_rooms:
        reservations = Reservation.objects.filter(
            room=room,
            check_in_date__lte=out_data,
            check_out_date__gte=in_data,
        )
        if reservations.exists():
            available_rooms = available_rooms.exclude(pk=room.pk)

    return available_rooms.values("number", "capacity", "comfort", "price")
