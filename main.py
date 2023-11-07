import sys
from datetime import date, datetime

import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from Windows.start_win import Ui_MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    user = Ui_MainWindow.user
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
