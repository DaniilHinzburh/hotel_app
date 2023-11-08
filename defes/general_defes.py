import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation, User, Settlement, Discount, Order
from decimal import Decimal


def fill_table_widget_with_data(queryset, table_widget):
    try:
        table_widget.clearContents()
        # Получаем данные из queryset
        data = list(queryset)

        if not data:
            return  # Если queryset пустой, не выполняем никаких действий

        # Устанавливаем количество строк и столбцов в виджете таблицы
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data[0]))

        # Получаем заголовки столбцов из ключей первой записи
        headers = list(data[0].keys())
        table_widget.setHorizontalHeaderLabels(headers)

        # Заполняем таблицу данными из queryset
        for row_index, row_data in enumerate(data):
            for col_index, field_name in enumerate(row_data.keys()):
                value = row_data[field_name]
                table_item = QtWidgets.QTableWidgetItem(str(value))
                table_widget.setItem(row_index, col_index, table_item)
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
        final_price *= (100 - discount.percent) / 100
    final_price = round(final_price, 2)
    return final_price


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


def get_user_discounts(user):
    try:
        return Discount.objects.filter(user=user).values("name", "percent")
    except Exception as e:
        print(e)


def get_user_by_passport(passport):
    try:
        return User.objects.get(passport=passport)
    except Exception as e:
        print(e)



