import sys
from datetime import date ,datetime

import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from Windows.start_win import Ui_MainWindow
from db.models import Reservation, User, Room

if __name__ == "__main__":
    # today = datetime.now().date()
    # new_reservation = Reservation.objects.create(
    #     user=User.objects.get(id=1),  # Замените user_instance на соответствующий объект User
    #     room=Room.objects.get(id=7),  # Замените room_instance на соответствующий объект Room
    #     check_in_date=date(2023, 11, 5),  # Установите нужное значение для check_in_date
    #     check_out_date=date(2023, 11, 6),  # Установите нужное значение для check_out_date
    # )
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    user = Ui_MainWindow.user
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
