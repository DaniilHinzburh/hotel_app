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

    return available_rooms
