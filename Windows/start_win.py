from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from Windows.create_user_win import create_user_win_MainWindow
from defes import sing_in_user


class Ui_MainWindow(object):
    user = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: DarkBlue ;\n"
                                   "border: 3px solid bleak;\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(238, 238, 238);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: DarkBlue ;\n"
                                   "border: 3px solid bleak;\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(238, 238, 238);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: DarkBlue ;\n"
                                   "border: 3px solid bleak;\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(238, 238, 238);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.err_label = QtWidgets.QLabel(self.centralwidget)
        self.err_label.setGeometry(QtCore.QRect(10, 320, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.err_label.setFont(font)
        self.err_label.setStyleSheet("color: rgb(231, 0, 0);")
        self.err_label.setText("")
        self.err_label.setAlignment(QtCore.Qt.AlignCenter)
        self.err_label.setObjectName("err_label")
        self.phone_text = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_text.setGeometry(QtCore.QRect(190, 160, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.phone_text.setFont(font)
        self.phone_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.phone_text.setStyleSheet("color: DarkBlue ;\n"
                                      "border: 3px solid bleak;\n"
                                      "border-radius: 20px;\n"
                                      "background-color: rgb(238, 238, 238);")
        self.phone_text.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_text.setObjectName("phone_text")
        self.pass_text = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_text.setGeometry(QtCore.QRect(190, 220, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pass_text.setFont(font)
        self.pass_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pass_text.setStyleSheet("color: DarkBlue ;\n"
                                     "border: 3px solid bleak;\n"
                                     "border-radius: 20px;\n"
                                     "background-color: rgb(238, 238, 238);")
        self.pass_text.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_text.setObjectName("pass_text")
        self.create_butt = QtWidgets.QPushButton(self.centralwidget)
        self.create_butt.setGeometry(QtCore.QRect(50, 490, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.create_butt.setFont(font)
        self.create_butt.setStyleSheet("QPushButton {\n"
                                       "    color: DarkBlue;\n"
                                       "    border: 3px solid bleak;\n"
                                       "    border-radius: 20px;\n"
                                       "    background-color: rgb(238, 238, 238);\n"
                                       "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                       "    padding: 5; /* Удаление внутренних отступов */\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: white;\n"
                                       "}\n"
                                       "")
        self.create_butt.setObjectName("create_butt")
        self.in_butt = QtWidgets.QPushButton(self.centralwidget)
        self.in_butt.setGeometry(QtCore.QRect(310, 490, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.in_butt.setFont(font)
        self.in_butt.setStyleSheet("QPushButton {\n"
                                   "    color: DarkBlue;\n"
                                   "    border: 3px solid bleak;\n"
                                   "    border-radius: 20px;\n"
                                   "    background-color: rgb(238, 238, 238);\n"
                                   "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                   "    padding: 5; /* Удаление внутренних отступов */\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: white;\n"
                                   "}\n"
                                   "")
        self.in_butt.setObjectName("in_butt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # назначение конопок
        self.create_butt.clicked.connect(self.open_create_user_window)
        self.in_butt.clicked.connect(lambda: self.user_in())

    # открытие окон
    def open_create_user_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = create_user_win_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()



    def err(self, text: str):
        self.err_label.setText(text)

    def user_in(self):
        self.user = sing_in_user.user_found(self.phone_text.text())

        if self.user is None:
            self.err("Помилка! Профіль не знайдено, створіть новий профіль")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Увійдіть у свій профіль"))
        self.label_3.setText(_translate("MainWindow", "Телефон"))
        self.label_4.setText(_translate("MainWindow", "Пароль"))
        self.create_butt.setText(_translate("MainWindow", "Створити профіль"))
        self.in_butt.setText(_translate("MainWindow", "Увійти"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
