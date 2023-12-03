import init_django_orm  # noqa: F401
from datetime import timedelta, datetime
from db.models import Room, Reservation, Discount, User, Order
from decimal import Decimal


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


def show_my_discount(user):
    return Discount.objects.filter(user=user).values("name", "percent")


def get_user_by_passport(passport):
    try:
        return User.objects.get(passport=passport)
    except Exception as e:
        print(e)


def get_reservation(user):
    return Reservation.objects.filter(user=user).values("room", "check_in_date", "check_out_date")


def delete_order(number: int):
    try:
        order = Order.objects.get(room=number)
        order.delete()
    except Exception:
        pass


def delete_reservation(number: int):
    try:
        reservation = Reservation.objects.get(room=number)
        delete_order(number)
        reservation.delete()
    except Exception:
        pass


def create_reservation(user, number, in_data, out_data, total_prise):
    room = Room.objects.get(number=number)
    reservation = Reservation.objects.create(
        user=user,
        room=room,
        check_in_date=in_data,
        check_out_date=out_data
    )

    reservation.save()
    create_order(user, number, in_data, out_data, total_prise)


def create_order(user, number, in_data, out_data, total_prise):
    try:
        room = Room.objects.get(number=number)
        order = Order.objects.create(
            user=user,
            room=room,
            check_in_date=in_data,
            check_out_date=out_data,
            price=total_prise
        )
        order.save()
    except Exception as e:
        print(e)


def count_total_price(number, num_days=None, check_in_date=None, check_out_date=None):
    try:
        if num_days is None:
            num_days = (check_out_date - check_in_date).days
        room = Room.objects.get(number=number)
        total_price = num_days * room.price
        return total_price
    except Exception:
        pass


def apply_discounts(user, price):
    user_discounts = user.discount.all()
    final_price = Decimal(price)
    if not user_discounts:
        return Decimal(price)
    for discount in user_discounts:
        final_price *= (100 - discount.percent) / 100
    final_price = round(final_price, 2)
    return final_price
