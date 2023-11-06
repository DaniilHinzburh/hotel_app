import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation


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


def find_available_rooms(comfort, capacity, num_of_days):
    # Получите сегодняшнюю дату
    today = datetime.now().date()
    # Вычислите дату выезда на основе количества дней
    check_out_date = today + timedelta(days=num_of_days)

    # Найдите номера, которые соответствуют критериям комфорта и вместимости
    available_rooms = Room.objects.filter(comfort=comfort, capacity=capacity)

    # Исключите номеры, которые забронированы на выбранный период
    for room in available_rooms:
        reservations = Reservation.objects.filter(
            room=room,
            check_in_date__lte=check_out_date,
            check_out_date__gte=today,
        )
        if reservations.exists():
            available_rooms = available_rooms.exclude(pk=room.pk)

    return available_rooms