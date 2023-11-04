import sys

import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from Windows.start_win import Ui_MainWindow
from db.models import User


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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    user = Ui_MainWindow.user
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
