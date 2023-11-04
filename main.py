import sys

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






    #     self.create_butt.clicked.connect(lambda: self.create_user())
    #
    # def create_user(self):
    #     user_list = [
    #         self.first_name_text.text(),
    #         self.last_name_text.text(),
    #         self.phone_text.text(),
    #         self.passpord_text.text(),
    #         self.passpord_text_2.text(),
    #         self.adress_text.text()
    #
    #     ]
    #
    #     if sing_in_user.create_user(*user_list):
    #         self.create_butt.setEnabled(False)
    #         self.create_butt.setText("Створено!")