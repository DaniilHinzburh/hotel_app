import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation, User, Settlement, Discount, Order
from decimal import Decimal


def fill_table_widget_with_data(queryset, table_widget):
    data = queryset

    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(
        len(data[0]._meta.fields))

    headers = [field.verbose_name for field in data[0]._meta.fields]
    table_widget.setHorizontalHeaderLabels(headers)

    for row_index, item in enumerate(data):
        for col_index, field in enumerate(item._meta.fields):
            value = getattr(item, field.name)
            table_item = QtWidgets.QTableWidgetItem(str(value))
            table_widget.setItem(row_index, col_index, table_item)


def count_total_price(number, num_days=None, check_in_date=None, check_out_date=None):
    try:
        if num_days is None:
            num_days = (check_out_date - check_in_date).days
        room = Room.objects.get(number=number)
        total_price = num_days * room.price
        return total_price
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


def create_settlement(user, number, in_data, out_data):
    room = Room.objects.get(number=number)
    settlement = Settlement.objects.create(
        user=user,
        room=room,
        check_in_date=in_data,
        check_out_date=out_data
    )
    settlement.save()


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


def apply_discounts(user, price):
    user_discounts = user.discount.all()
    final_price = Decimal(price)
    if not user_discounts:
        return Decimal(price)
    for discount in user_discounts:
        final_price *= discount.percent
    final_price = round(final_price, 2)
    return final_price


def get_reservation(user):
    return Reservation.objects.filter(user=user)
