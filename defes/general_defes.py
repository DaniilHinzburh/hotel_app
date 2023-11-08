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


def get_user_discounts(user):
    try:
        return Discount.objects.filter(user=user).values("name", "percent")
    except Exception as e:
        print(e)
