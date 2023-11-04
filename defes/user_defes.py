import init_django_orm  # noqa: F401
import db.models
from PyQt5 import QtWidgets


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
