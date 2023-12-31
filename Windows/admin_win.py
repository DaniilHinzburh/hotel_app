from PyQt5 import QtCore, QtGui, QtWidgets
from defes import admin_win_defes


class Admin_win(object):
    user = None
    room = None
    discount = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        Dialog.setMinimumSize(QtCore.QSize(800, 800))
        Dialog.setMaximumSize(QtCore.QSize(800, 800))
        Dialog.setSizeIncrement(QtCore.QSize(800, 800))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 780, 780))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
                                     "    color: rgb(172, 85, 27);\n"
                                     "    border: 2px solid bleak;\n"
                                     "    border-radius: 20px;\n"
                                     "    background-color: rgb(238, 238, 238);\n"
                                     "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                     "    padding: 10; /* Удаление внутренних отступов */\n"
                                     "    margin: 5px;\n"
                                     "    alignment: center;\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    background-color: white;\n"
                                     "}\n"
                                     "           QTabWidget::tab-bar {\n"
                                     "                alignment: center;\n"
                                     "            }")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.table_user = QtWidgets.QTableWidget(self.tab_1)
        self.table_user.setGeometry(QtCore.QRect(15, 70, 741, 151))
        self.table_user.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 16px;} QTableWidget::item {font-weight: bold;}")
        self.table_user.setObjectName("table_user")
        self.table_user.setColumnCount(0)
        self.table_user.setRowCount(0)
        # header = self.table_user.horizontalHeader()
        # header.setFont(QtGui.QFont("Arial", 14))
        self.table_user.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_1_show_table_useer_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_show_table_useer_butt.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_show_table_useer_butt.setFont(font)
        self.tab_1_show_table_useer_butt.setStyleSheet("QPushButton {\n"
                                                       "    color: rgb(172, 85, 27);\n"
                                                       "    border: 3px solid bleak;\n"
                                                       "    border-radius: 20px;\n"
                                                       "    background-color: rgb(238, 238, 238);\n"
                                                       "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                       "    padding: 0; /* Удаление внутренних отступов */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover {\n"
                                                       "    background-color: white;\n"
                                                       "}\n"
                                                       "")
        self.tab_1_show_table_useer_butt.setObjectName("tab_1_show_table_useer_butt")
        self.tab_1_passport_in = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_passport_in.setGeometry(QtCore.QRect(210, 240, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_passport_in.setFont(font)
        self.tab_1_passport_in.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                             "border: 3px solid bleak;\n"
                                             "border-radius: 20px;\n"
                                             "background-color: rgb(238, 238, 238);\n"
                                             "")
        self.tab_1_passport_in.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_passport_in.setObjectName("tab_1_passport_in")
        self.label_10 = QtWidgets.QLabel(self.tab_1)
        self.label_10.setGeometry(QtCore.QRect(18, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.tab_1_delete_user_dutt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_delete_user_dutt.setEnabled(False)
        self.tab_1_delete_user_dutt.setGeometry(QtCore.QRect(20, 450, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_delete_user_dutt.setFont(font)
        self.tab_1_delete_user_dutt.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(172, 85, 27);\n"
                                                  "    border: 3px solid bleak;\n"
                                                  "    border-radius: 20px;\n"
                                                  "    background-color: rgb(238, 238, 238);\n"
                                                  "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                  "    padding: 0; /* Удаление внутренних отступов */\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: white;\n"
                                                  "}\n"
                                                  "")
        self.tab_1_delete_user_dutt.setObjectName("tab_1_delete_user_dutt")
        self.tab_1_get_user_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_get_user_butt.setEnabled(True)
        self.tab_1_get_user_butt.setGeometry(QtCore.QRect(480, 240, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_get_user_butt.setFont(font)
        self.tab_1_get_user_butt.setStyleSheet("QPushButton {\n"
                                               "    color: rgb(172, 85, 27);\n"
                                               "    border: 3px solid bleak;\n"
                                               "    border-radius: 20px;\n"
                                               "    background-color: rgb(238, 238, 238);\n"
                                               "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                               "    padding: 0; /* Удаление внутренних отступов */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: white;\n"
                                               "}\n"
                                               "")
        self.tab_1_get_user_butt.setObjectName("tab_1_get_user_butt")
        self.tab_1_update_user_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_update_user_butt.setEnabled(False)
        self.tab_1_update_user_butt.setGeometry(QtCore.QRect(540, 450, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_update_user_butt.setFont(font)
        self.tab_1_update_user_butt.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(172, 85, 27);\n"
                                                  "    border: 3px solid bleak;\n"
                                                  "    border-radius: 20px;\n"
                                                  "    background-color: rgb(238, 238, 238);\n"
                                                  "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                  "    padding: 0; /* Удаление внутренних отступов */\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: white;\n"
                                                  "}\n"
                                                  "")
        self.tab_1_update_user_butt.setObjectName("tab_1_update_user_butt")
        self.tab_1_first_name = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_first_name.setGeometry(QtCore.QRect(20, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_first_name.setFont(font)
        self.tab_1_first_name.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                            "border: 3px solid bleak;\n"
                                            "border-radius: 20px;\n"
                                            "background-color: rgb(238, 238, 238);\n"
                                            "")
        self.tab_1_first_name.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_first_name.setObjectName("tab_1_first_name")
        self.tab_1_last_name = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_last_name.setGeometry(QtCore.QRect(280, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_last_name.setFont(font)
        self.tab_1_last_name.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                           "border: 3px solid bleak;\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(238, 238, 238);\n"
                                           "")
        self.tab_1_last_name.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_last_name.setObjectName("tab_1_last_name")
        self.tab_1_password = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_password.setGeometry(QtCore.QRect(540, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_password.setFont(font)
        self.tab_1_password.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                          "border: 3px solid bleak;\n"
                                          "border-radius: 20px;\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "")
        self.tab_1_password.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_password.setObjectName("tab_1_password")
        self.tab_1_adress = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_adress.setGeometry(QtCore.QRect(280, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_adress.setFont(font)
        self.tab_1_adress.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                        "border: 3px solid bleak;\n"
                                        "border-radius: 20px;\n"
                                        "background-color: rgb(238, 238, 238);\n"
                                        "")
        self.tab_1_adress.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_adress.setObjectName("tab_1_adress")
        self.tab_1_phone = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_phone.setGeometry(QtCore.QRect(20, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_phone.setFont(font)
        self.tab_1_phone.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                       "border: 3px solid bleak;\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(238, 238, 238);\n"
                                       "")
        self.tab_1_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_phone.setObjectName("tab_1_phone")
        self.tab_1_comment = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_comment.setGeometry(QtCore.QRect(540, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_comment.setFont(font)
        self.tab_1_comment.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                         "border: 3px solid bleak;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: rgb(238, 238, 238);\n"
                                         "")
        self.tab_1_comment.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_comment.setObjectName("tab_1_comment")
        self.table_user_dis = QtWidgets.QTableWidget(self.tab_1)
        self.table_user_dis.setGeometry(QtCore.QRect(20, 560, 311, 151))
        self.table_user_dis.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;} ")
        self.table_user_dis.setObjectName("table_user_dis")
        self.table_user_dis.setColumnCount(0)
        self.table_user_dis.setRowCount(0)
        header = self.table_user_dis.horizontalHeader()
        header.setFont(QtGui.QFont("Arial", 14))
        self.table_user_dis.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_1_add_dis_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_add_dis_butt.setEnabled(False)
        self.tab_1_add_dis_butt.setGeometry(QtCore.QRect(340, 670, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_add_dis_butt.setFont(font)
        self.tab_1_add_dis_butt.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(172, 85, 27);\n"
                                              "    border: 3px solid bleak;\n"
                                              "    border-radius: 20px;\n"
                                              "    background-color: rgb(238, 238, 238);\n"
                                              "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                              "    padding: 0; /* Удаление внутренних отступов */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: white;\n"
                                              "}\n"
                                              "")
        self.tab_1_add_dis_butt.setObjectName("tab_1_add_dis_butt")
        self.tab_1_dell_dis_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_dell_dis_butt.setEnabled(False)
        self.tab_1_dell_dis_butt.setGeometry(QtCore.QRect(560, 670, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_dell_dis_butt.setFont(font)
        self.tab_1_dell_dis_butt.setStyleSheet("QPushButton {\n"
                                               "    color: rgb(172, 85, 27);\n"
                                               "    border: 3px solid bleak;\n"
                                               "    border-radius: 20px;\n"
                                               "    background-color: rgb(238, 238, 238);\n"
                                               "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                               "    padding: 0; /* Удаление внутренних отступов */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: white;\n"
                                               "}\n"
                                               "")
        self.tab_1_dell_dis_butt.setObjectName("tab_1_dell_dis_butt")
        self.label_11 = QtWidgets.QLabel(self.tab_1)
        self.label_11.setGeometry(QtCore.QRect(340, 560, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tab_1_dis_name = QtWidgets.QLineEdit(self.tab_1)
        self.tab_1_dis_name.setGeometry(QtCore.QRect(560, 560, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_dis_name.setFont(font)
        self.tab_1_dis_name.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                          "border: 3px solid bleak;\n"
                                          "border-radius: 20px;\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "")
        self.tab_1_dis_name.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_1_dis_name.setObjectName("tab_1_dis_name")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.table_room = QtWidgets.QTableWidget(self.tab_2)
        self.table_room.setGeometry(QtCore.QRect(15, 70, 741, 151))
        self.table_room.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;}")
        self.table_room.setObjectName("table_room")
        self.table_room.setColumnCount(0)
        self.table_room.setRowCount(0)
        # header = self.table_room.horizontalHeader()
        # header.setFont(QtGui.QFont("Arial", 14))
        self.table_room.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_2_show_table_room = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_show_table_room.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_show_table_room.setFont(font)
        self.tab_2_show_table_room.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(172, 85, 27);\n"
                                                 "    border: 3px solid bleak;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                 "    padding: 0; /* Удаление внутренних отступов */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: white;\n"
                                                 "}\n"
                                                 "")
        self.tab_2_show_table_room.setObjectName("tab_2_show_table_room")
        self.tab_2_update_room_butt = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_update_room_butt.setEnabled(False)
        self.tab_2_update_room_butt.setGeometry(QtCore.QRect(540, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_update_room_butt.setFont(font)
        self.tab_2_update_room_butt.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(172, 85, 27);\n"
                                                  "    border: 3px solid bleak;\n"
                                                  "    border-radius: 20px;\n"
                                                  "    background-color: rgb(238, 238, 238);\n"
                                                  "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                  "    padding: 0; /* Удаление внутренних отступов */\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: white;\n"
                                                  "}\n"
                                                  "")
        self.tab_2_update_room_butt.setObjectName("tab_2_update_room_butt")
        self.tab_2_comfort = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_comfort.setGeometry(QtCore.QRect(280, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_comfort.setFont(font)
        self.tab_2_comfort.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                         "border: 3px solid bleak;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: rgb(238, 238, 238);\n"
                                         "")
        self.tab_2_comfort.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_comfort.setObjectName("tab_2_comfort")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(18, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.tab_2_number_in = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_number_in.setGeometry(QtCore.QRect(210, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_number_in.setFont(font)
        self.tab_2_number_in.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                           "border: 3px solid bleak;\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(238, 238, 238);\n"
                                           "")
        self.tab_2_number_in.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_number_in.setObjectName("tab_2_number_in")
        self.tab_2_delete_room_butt = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_delete_room_butt.setEnabled(False)
        self.tab_2_delete_room_butt.setGeometry(QtCore.QRect(20, 370, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_delete_room_butt.setFont(font)
        self.tab_2_delete_room_butt.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(172, 85, 27);\n"
                                                  "    border: 3px solid bleak;\n"
                                                  "    border-radius: 20px;\n"
                                                  "    background-color: rgb(238, 238, 238);\n"
                                                  "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                  "    padding: 0; /* Удаление внутренних отступов */\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: white;\n"
                                                  "}\n"
                                                  "")
        self.tab_2_delete_room_butt.setObjectName("tab_2_delete_room_butt")
        self.tab_2_capacity = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_capacity.setGeometry(QtCore.QRect(20, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_capacity.setFont(font)
        self.tab_2_capacity.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                          "border: 3px solid bleak;\n"
                                          "border-radius: 20px;\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "")
        self.tab_2_capacity.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_capacity.setObjectName("tab_2_capacity")
        self.tab_2_price = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_price.setGeometry(QtCore.QRect(540, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_price.setFont(font)
        self.tab_2_price.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                       "border: 3px solid bleak;\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(238, 238, 238);\n"
                                       "")
        self.tab_2_price.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_price.setObjectName("tab_2_price")
        self.tab_2_get_room_butt = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_get_room_butt.setEnabled(True)
        self.tab_2_get_room_butt.setGeometry(QtCore.QRect(480, 240, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_get_room_butt.setFont(font)
        self.tab_2_get_room_butt.setStyleSheet("QPushButton {\n"
                                               "    color: rgb(172, 85, 27);\n"
                                               "    border: 3px solid bleak;\n"
                                               "    border-radius: 20px;\n"
                                               "    background-color: rgb(238, 238, 238);\n"
                                               "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                               "    padding: 0; /* Удаление внутренних отступов */\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background-color: white;\n"
                                               "}\n"
                                               "")
        self.tab_2_get_room_butt.setObjectName("tab_2_get_room_butt")
        self.tab_2_price_new_room = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_price_new_room.setGeometry(QtCore.QRect(280, 660, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_price_new_room.setFont(font)
        self.tab_2_price_new_room.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                "border: 3px solid bleak;\n"
                                                "border-radius: 20px;\n"
                                                "background-color: rgb(238, 238, 238);\n"
                                                "")
        self.tab_2_price_new_room.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_price_new_room.setObjectName("tab_2_price_new_room")
        self.tab_2_capacity_new_room = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_capacity_new_room.setGeometry(QtCore.QRect(280, 540, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_capacity_new_room.setFont(font)
        self.tab_2_capacity_new_room.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                   "border: 3px solid bleak;\n"
                                                   "border-radius: 20px;\n"
                                                   "background-color: rgb(238, 238, 238);\n"
                                                   "")
        self.tab_2_capacity_new_room.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_capacity_new_room.setObjectName("tab_2_capacity_new_room")
        self.tab_2_comfort_new_room = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_comfort_new_room.setGeometry(QtCore.QRect(280, 600, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_comfort_new_room.setFont(font)
        self.tab_2_comfort_new_room.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                  "border: 3px solid bleak;\n"
                                                  "border-radius: 20px;\n"
                                                  "background-color: rgb(238, 238, 238);\n"
                                                  "")
        self.tab_2_comfort_new_room.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_comfort_new_room.setObjectName("tab_2_comfort_new_room")
        self.tab_2_number_new_room = QtWidgets.QLineEdit(self.tab_2)
        self.tab_2_number_new_room.setGeometry(QtCore.QRect(280, 480, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_number_new_room.setFont(font)
        self.tab_2_number_new_room.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                 "border: 3px solid bleak;\n"
                                                 "border-radius: 20px;\n"
                                                 "background-color: rgb(238, 238, 238);\n"
                                                 "")
        self.tab_2_number_new_room.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_2_number_new_room.setObjectName("tab_2_number_new_room")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 480, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(20, 540, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(20, 600, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(20, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.tab_2_create_room_butt = QtWidgets.QPushButton(self.tab_2)
        self.tab_2_create_room_butt.setEnabled(True)
        self.tab_2_create_room_butt.setGeometry(QtCore.QRect(540, 570, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_create_room_butt.setFont(font)
        self.tab_2_create_room_butt.setStyleSheet("QPushButton {\n"
                                                  "    color: rgb(172, 85, 27);\n"
                                                  "    border: 3px solid bleak;\n"
                                                  "    border-radius: 20px;\n"
                                                  "    background-color: rgb(238, 238, 238);\n"
                                                  "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                  "    padding: 0; /* Удаление внутренних отступов */\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "    background-color: white;\n"
                                                  "}\n"
                                                  "")
        self.tab_2_create_room_butt.setObjectName("tab_2_create_room_butt")
        self.label_3.raise_()
        self.table_room.raise_()
        self.tab_2_show_table_room.raise_()
        self.tab_2_update_room_butt.raise_()
        self.tab_2_comfort.raise_()
        self.label_12.raise_()
        self.tab_2_number_in.raise_()
        self.tab_2_delete_room_butt.raise_()
        self.tab_2_capacity.raise_()
        self.tab_2_price.raise_()
        self.tab_2_get_room_butt.raise_()
        self.tab_2_price_new_room.raise_()
        self.tab_2_capacity_new_room.raise_()
        self.tab_2_comfort_new_room.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.tab_2_create_room_butt.raise_()
        self.tab_2_number_new_room.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tab_3_show_table_dis_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_3_show_table_dis_butt.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_show_table_dis_butt.setFont(font)
        self.tab_3_show_table_dis_butt.setStyleSheet("QPushButton {\n"
                                                     "    color: rgb(172, 85, 27);\n"
                                                     "    border: 3px solid bleak;\n"
                                                     "    border-radius: 20px;\n"
                                                     "    background-color: rgb(238, 238, 238);\n"
                                                     "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                     "    padding: 0; /* Удаление внутренних отступов */\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: white;\n"
                                                     "}\n"
                                                     "")
        self.tab_3_show_table_dis_butt.setObjectName("tab_3_show_table_dis_butt")
        self.table_dis = QtWidgets.QTableWidget(self.tab_3)
        self.table_dis.setGeometry(QtCore.QRect(15, 70, 741, 151))
        self.table_dis.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;}")
        self.table_dis.setObjectName("table_dis")
        self.table_dis.setColumnCount(0)
        self.table_dis.setRowCount(0)
        header = self.table_dis.horizontalHeader()
        header.setFont(QtGui.QFont("Arial", 14))
        self.table_dis.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_3_update_dis_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_3_update_dis_butt.setEnabled(True)
        self.tab_3_update_dis_butt.setGeometry(QtCore.QRect(250, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_update_dis_butt.setFont(font)
        self.tab_3_update_dis_butt.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(172, 85, 27);\n"
                                                 "    border: 3px solid bleak;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                 "    padding: 0; /* Удаление внутренних отступов */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: white;\n"
                                                 "}\n"
                                                 "")
        self.tab_3_update_dis_butt.setObjectName("tab_3_update_dis_butt")
        self.tab_3_percent_dis = QtWidgets.QLineEdit(self.tab_3)
        self.tab_3_percent_dis.setGeometry(QtCore.QRect(20, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_percent_dis.setFont(font)
        self.tab_3_percent_dis.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                             "border: 3px solid bleak;\n"
                                             "border-radius: 20px;\n"
                                             "background-color: rgb(238, 238, 238);\n"
                                             "")
        self.tab_3_percent_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_3_percent_dis.setObjectName("tab_3_percent_dis")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(18, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(20, 540, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.tab_3_name_dis = QtWidgets.QLineEdit(self.tab_3)
        self.tab_3_name_dis.setGeometry(QtCore.QRect(210, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_name_dis.setFont(font)
        self.tab_3_name_dis.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                          "border: 3px solid bleak;\n"
                                          "border-radius: 20px;\n"
                                          "background-color: rgb(238, 238, 238);\n"
                                          "")
        self.tab_3_name_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_3_name_dis.setObjectName("tab_3_name_dis")
        self.tab_3_name_new_dis = QtWidgets.QLineEdit(self.tab_3)
        self.tab_3_name_new_dis.setGeometry(QtCore.QRect(280, 480, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_name_new_dis.setFont(font)
        self.tab_3_name_new_dis.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                              "border: 3px solid bleak;\n"
                                              "border-radius: 20px;\n"
                                              "background-color: rgb(238, 238, 238);\n"
                                              "")
        self.tab_3_name_new_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_3_name_new_dis.setObjectName("tab_3_name_new_dis")
        self.tab_3_get_dis_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_3_get_dis_butt.setEnabled(True)
        self.tab_3_get_dis_butt.setGeometry(QtCore.QRect(480, 240, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_get_dis_butt.setFont(font)
        self.tab_3_get_dis_butt.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(172, 85, 27);\n"
                                              "    border: 3px solid bleak;\n"
                                              "    border-radius: 20px;\n"
                                              "    background-color: rgb(238, 238, 238);\n"
                                              "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                              "    padding: 0; /* Удаление внутренних отступов */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: white;\n"
                                              "}\n"
                                              "")
        self.tab_3_get_dis_butt.setObjectName("tab_3_get_dis_butt")
        self.tab_3_create_dis_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_3_create_dis_butt.setEnabled(True)
        self.tab_3_create_dis_butt.setGeometry(QtCore.QRect(280, 600, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_create_dis_butt.setFont(font)
        self.tab_3_create_dis_butt.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(172, 85, 27);\n"
                                                 "    border: 3px solid bleak;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                 "    padding: 0; /* Удаление внутренних отступов */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: white;\n"
                                                 "}\n"
                                                 "")
        self.tab_3_create_dis_butt.setObjectName("tab_3_create_dis_butt")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(20, 480, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.tab_3_name_dis_2 = QtWidgets.QLineEdit(self.tab_3)
        self.tab_3_name_dis_2.setGeometry(QtCore.QRect(20, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_name_dis_2.setFont(font)
        self.tab_3_name_dis_2.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                            "border: 3px solid bleak;\n"
                                            "border-radius: 20px;\n"
                                            "background-color: rgb(238, 238, 238);\n"
                                            "")
        self.tab_3_name_dis_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_3_name_dis_2.setObjectName("tab_3_name_dis_2")
        self.tab_3_percent_new_dis = QtWidgets.QLineEdit(self.tab_3)
        self.tab_3_percent_new_dis.setGeometry(QtCore.QRect(280, 540, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_percent_new_dis.setFont(font)
        self.tab_3_percent_new_dis.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                 "border: 3px solid bleak;\n"
                                                 "border-radius: 20px;\n"
                                                 "background-color: rgb(238, 238, 238);\n"
                                                 "")
        self.tab_3_percent_new_dis.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_3_percent_new_dis.setObjectName("tab_3_percent_new_dis")
        self.tab_3_delete_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_3_delete_butt.setEnabled(True)
        self.tab_3_delete_butt.setGeometry(QtCore.QRect(250, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_3_delete_butt.setFont(font)
        self.tab_3_delete_butt.setStyleSheet("QPushButton {\n"
                                             "    color: rgb(172, 85, 27);\n"
                                             "    border: 3px solid bleak;\n"
                                             "    border-radius: 20px;\n"
                                             "    background-color: rgb(238, 238, 238);\n"
                                             "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                             "    padding: 0; /* Удаление внутренних отступов */\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    background-color: white;\n"
                                             "}\n"
                                             "")
        self.tab_3_delete_butt.setObjectName("tab_3_delete_butt")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(20, 660, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.table_res = QtWidgets.QTableWidget(self.tab_4)
        self.table_res.setGeometry(QtCore.QRect(15, 70, 741, 571))
        self.table_res.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;}")
        self.table_res.setObjectName("table_res")
        self.table_res.setColumnCount(0)
        self.table_res.setRowCount(0)
        header = self.table_res.horizontalHeader()
        header.setFont(QtGui.QFont("Arial", 14))
        self.table_res.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_4_show_table_res_butt = QtWidgets.QPushButton(self.tab_4)
        self.tab_4_show_table_res_butt.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_4_show_table_res_butt.setFont(font)
        self.tab_4_show_table_res_butt.setStyleSheet("QPushButton {\n"
                                                     "    color: rgb(172, 85, 27);\n"
                                                     "    border: 3px solid bleak;\n"
                                                     "    border-radius: 20px;\n"
                                                     "    background-color: rgb(238, 238, 238);\n"
                                                     "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                     "    padding: 0; /* Удаление внутренних отступов */\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: white;\n"
                                                     "}\n"
                                                     "")
        self.tab_4_show_table_res_butt.setObjectName("tab_4_show_table_res_butt")
        self.tab_4_id_res = QtWidgets.QLineEdit(self.tab_4)
        self.tab_4_id_res.setGeometry(QtCore.QRect(142, 660, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_4_id_res.setFont(font)
        self.tab_4_id_res.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                        "border: 3px solid bleak;\n"
                                        "border-radius: 20px;\n"
                                        "background-color: rgb(238, 238, 238);\n"
                                        "")
        self.tab_4_id_res.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_4_id_res.setObjectName("tab_4_id_res")
        self.tab_4_delete_res_butt = QtWidgets.QPushButton(self.tab_4)
        self.tab_4_delete_res_butt.setEnabled(False)
        self.tab_4_delete_res_butt.setGeometry(QtCore.QRect(482, 660, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_4_delete_res_butt.setFont(font)
        self.tab_4_delete_res_butt.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(172, 85, 27);\n"
                                                 "    border: 3px solid bleak;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                 "    padding: 0; /* Удаление внутренних отступов */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: white;\n"
                                                 "}\n"
                                                 "")
        self.tab_4_delete_res_butt.setObjectName("tab_4_delete_res_butt")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.tab_5_show_table_order_butt = QtWidgets.QPushButton(self.tab_6)
        self.tab_5_show_table_order_butt.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_5_show_table_order_butt.setFont(font)
        self.tab_5_show_table_order_butt.setStyleSheet("QPushButton {\n"
                                                       "    color: rgb(172, 85, 27);\n"
                                                       "    border: 3px solid bleak;\n"
                                                       "    border-radius: 20px;\n"
                                                       "    background-color: rgb(238, 238, 238);\n"
                                                       "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                       "    padding: 0; /* Удаление внутренних отступов */\n"
                                                       "}\n"
                                                       "\n"
                                                       "QPushButton:hover {\n"
                                                       "    background-color: white;\n"
                                                       "}\n"
                                                       "")
        self.tab_5_show_table_order_butt.setObjectName("tab_5_show_table_order_butt")
        self.table_order = QtWidgets.QTableWidget(self.tab_6)
        self.table_order.setGeometry(QtCore.QRect(15, 70, 741, 631))
        self.table_order.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;}")
        self.table_order.setObjectName("table_order")
        self.table_order.setColumnCount(0)
        self.table_order.setRowCount(0)
        # header = self.table_order.horizontalHeader()
        # header.setFont(QtGui.QFont("Arial", 14))
        self.table_order.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_9 = QtWidgets.QLabel(self.tab_7)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 780, 780))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/admin.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.table_settlement = QtWidgets.QTableWidget(self.tab_7)
        self.table_settlement.setGeometry(QtCore.QRect(15, 70, 741, 151))
        self.table_settlement.setStyleSheet(
            "QTableWidget {color: rgb(172, 85, 27);font-size: 24px;} QTableWidget::item {font-weight: bold;}")
        self.table_settlement.setObjectName("table_settlement")
        self.table_settlement.setColumnCount(0)
        self.table_settlement.setRowCount(0)
        header = self.table_settlement.horizontalHeader()
        header.setFont(QtGui.QFont("Arial", 14))
        self.table_settlement.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab_6_show_table_settlement_butt = QtWidgets.QPushButton(self.tab_7)
        self.tab_6_show_table_settlement_butt.setGeometry(QtCore.QRect(20, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_show_table_settlement_butt.setFont(font)
        self.tab_6_show_table_settlement_butt.setStyleSheet("QPushButton {\n"
                                                            "    color: rgb(172, 85, 27);\n"
                                                            "    border: 3px solid bleak;\n"
                                                            "    border-radius: 20px;\n"
                                                            "    background-color: rgb(238, 238, 238);\n"
                                                            "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                            "    padding: 0; /* Удаление внутренних отступов */\n"
                                                            "}\n"
                                                            "\n"
                                                            "QPushButton:hover {\n"
                                                            "    background-color: white;\n"
                                                            "}\n"
                                                            "")
        self.tab_6_show_table_settlement_butt.setObjectName("tab_6_show_table_settlement_butt")
        self.tab_6_passport_on_sett = QtWidgets.QLineEdit(self.tab_7)
        self.tab_6_passport_on_sett.setGeometry(QtCore.QRect(210, 280, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_passport_on_sett.setFont(font)
        self.tab_6_passport_on_sett.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                  "border: 3px solid bleak;\n"
                                                  "border-radius: 20px;\n"
                                                  "background-color: rgb(238, 238, 238);\n"
                                                  "")
        self.tab_6_passport_on_sett.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_6_passport_on_sett.setObjectName("tab_6_passport_on_sett")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(20, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.tab_6_on_sett_butt = QtWidgets.QPushButton(self.tab_7)
        self.tab_6_on_sett_butt.setEnabled(True)
        self.tab_6_on_sett_butt.setGeometry(QtCore.QRect(460, 340, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_on_sett_butt.setFont(font)
        self.tab_6_on_sett_butt.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(172, 85, 27);\n"
                                              "    border: 3px solid bleak;\n"
                                              "    border-radius: 20px;\n"
                                              "    background-color: rgb(238, 238, 238);\n"
                                              "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                              "    padding: 0; /* Удаление внутренних отступов */\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: white;\n"
                                              "}\n"
                                              "")
        self.tab_6_on_sett_butt.setObjectName("tab_6_on_sett_butt")
        self.label_22 = QtWidgets.QLabel(self.tab_7)
        self.label_22.setGeometry(QtCore.QRect(100, 230, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.tab_6_room_num_on_sett = QtWidgets.QLineEdit(self.tab_7)
        self.tab_6_room_num_on_sett.setGeometry(QtCore.QRect(210, 340, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_room_num_on_sett.setFont(font)
        self.tab_6_room_num_on_sett.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                  "border: 3px solid bleak;\n"
                                                  "border-radius: 20px;\n"
                                                  "background-color: rgb(238, 238, 238);\n"
                                                  "")
        self.tab_6_room_num_on_sett.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_6_room_num_on_sett.setObjectName("tab_6_room_num_on_sett")
        self.label_23 = QtWidgets.QLabel(self.tab_7)
        self.label_23.setGeometry(QtCore.QRect(20, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.tab_6_data_in = QtWidgets.QLineEdit(self.tab_7)
        self.tab_6_data_in.setGeometry(QtCore.QRect(210, 400, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_data_in.setFont(font)
        self.tab_6_data_in.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                         "border: 3px solid bleak;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: rgb(238, 238, 238);\n"
                                         "")
        self.tab_6_data_in.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_6_data_in.setObjectName("tab_6_data_in")
        self.label_24 = QtWidgets.QLabel(self.tab_7)
        self.label_24.setGeometry(QtCore.QRect(20, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.tab_6_room_num_close_sett = QtWidgets.QLineEdit(self.tab_7)
        self.tab_6_room_num_close_sett.setGeometry(QtCore.QRect(210, 600, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_room_num_close_sett.setFont(font)
        self.tab_6_room_num_close_sett.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                     "border: 3px solid bleak;\n"
                                                     "border-radius: 20px;\n"
                                                     "background-color: rgb(238, 238, 238);\n"
                                                     "")
        self.tab_6_room_num_close_sett.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_6_room_num_close_sett.setObjectName("tab_6_room_num_close_sett")
        self.tab_6_passport_close_sett = QtWidgets.QLineEdit(self.tab_7)
        self.tab_6_passport_close_sett.setGeometry(QtCore.QRect(210, 540, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_passport_close_sett.setFont(font)
        self.tab_6_passport_close_sett.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                                     "border: 3px solid bleak;\n"
                                                     "border-radius: 20px;\n"
                                                     "background-color: rgb(238, 238, 238);\n"
                                                     "")
        self.tab_6_passport_close_sett.setAlignment(QtCore.Qt.AlignCenter)
        self.tab_6_passport_close_sett.setObjectName("tab_6_passport_close_sett")
        self.label_26 = QtWidgets.QLabel(self.tab_7)
        self.label_26.setGeometry(QtCore.QRect(20, 540, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_7)
        self.label_27.setGeometry(QtCore.QRect(20, 600, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.tab_6_close_sett_butt = QtWidgets.QPushButton(self.tab_7)
        self.tab_6_close_sett_butt.setEnabled(True)
        self.tab_6_close_sett_butt.setGeometry(QtCore.QRect(450, 570, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_6_close_sett_butt.setFont(font)
        self.tab_6_close_sett_butt.setStyleSheet("QPushButton {\n"
                                                 "    color: rgb(172, 85, 27);\n"
                                                 "    border: 3px solid bleak;\n"
                                                 "    border-radius: 20px;\n"
                                                 "    background-color: rgb(238, 238, 238);\n"
                                                 "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                                                 "    padding: 0; /* Удаление внутренних отступов */\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: white;\n"
                                                 "}\n"
                                                 "")
        self.tab_6_close_sett_butt.setObjectName("tab_6_close_sett_butt")
        self.label_28 = QtWidgets.QLabel(self.tab_7)
        self.label_28.setGeometry(QtCore.QRect(90, 470, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(172, 85, 27) ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # кнопки tab_1
        self.tab_1_show_table_useer_butt.clicked.connect(lambda: admin_win_defes.tab_1_show_table_user(self))
        self.tab_1_get_user_butt.clicked.connect(lambda: admin_win_defes.tab_1_get_user_butt_clicked(self))
        self.tab_1_update_user_butt.clicked.connect(lambda: admin_win_defes.tab_1_update_user_butt_clicked(self))
        self.tab_1_delete_user_dutt.clicked.connect(lambda: admin_win_defes.tab_1_delete_user_butt_clicked(self))
        self.tab_1_dell_dis_butt.clicked.connect(lambda: admin_win_defes.tab_1_dell_dis_butt_clicked(self))
        self.tab_1_add_dis_butt.clicked.connect(lambda: admin_win_defes.tab_1_add_dis_butt_clicked(self))
        # кнопки tab_2
        self.tab_2_show_table_room.clicked.connect(lambda: admin_win_defes.tab_2_show_table_room_clicked(self))
        self.tab_2_get_room_butt.clicked.connect(lambda: admin_win_defes.tab_2_get_room_butt_clicked(self))
        self.tab_2_delete_room_butt.clicked.connect(lambda: admin_win_defes.tab_2_delete_room_butt_clicked(self))
        self.tab_2_update_room_butt.clicked.connect(lambda: admin_win_defes.tab_2_update_room_butt_clicked(self))
        self.tab_2_create_room_butt.clicked.connect(lambda: admin_win_defes.tab_2_create_room_butt_clicked(self))
        # кнопки tab_3
        self.tab_3_show_table_dis_butt.clicked.connect(lambda: admin_win_defes.tab_3_show_table_dis_butt_clicked(self))
        self.tab_3_get_dis_butt.clicked.connect(lambda: admin_win_defes.tab_3_get_dis_butt_clicked(self))
        self.tab_3_delete_butt.clicked.connect(lambda: admin_win_defes.tab_3_delete_butt_clicked(self))
        self.tab_3_update_dis_butt.clicked.connect(lambda: admin_win_defes.tab_3_update_dis_butt_clicked(self))
        self.tab_3_create_dis_butt.clicked.connect(lambda: admin_win_defes.tab_3_create_dis_butt_clicked(self))
        # кнопки tab_4
        self.tab_4_show_table_res_butt.clicked.connect(lambda: admin_win_defes.tab_4_show_table_res_butt_clicked(self))
        self.tab_4_delete_res_butt.clicked.connect(lambda: admin_win_defes.tab_4_delete_res_butt_clicked(self))
        # кнопки tab_5
        self.tab_5_show_table_order_butt.clicked.connect(lambda: admin_win_defes.tab_5_show_table_order_butt_clicked(self))
        # кнопки tab_6
        self.tab_6_show_table_settlement_butt.clicked.connect(lambda: admin_win_defes.tab_6_show_table_settlement_butt_clicked(self))
        self.tab_6_on_sett_butt.clicked.connect(lambda: admin_win_defes.tab_6_on_sett_butt_clicked(self))
        self.tab_6_close_sett_butt.clicked.connect(lambda: admin_win_defes.tab_6_close_sett_butt_clicked(self))



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tab_1_show_table_useer_butt.setText(_translate("Dialog", "Вивести данні всіх користувачів"))
        self.label_10.setText(_translate("Dialog", "Номер паспорту:"))
        self.tab_1_delete_user_dutt.setText(_translate("Dialog", "Видалити користувача"))
        self.tab_1_get_user_butt.setText(_translate("Dialog", "Отримати данні користувача"))
        self.tab_1_update_user_butt.setText(_translate("Dialog", "Змінити данні"))
        self.tab_1_add_dis_butt.setText(_translate("Dialog", "Додати знижку"))
        self.tab_1_dell_dis_butt.setText(_translate("Dialog", "Видалити знижку"))
        self.label_11.setText(_translate("Dialog", "Назва знижки: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Dialog", "Список користувачів"))
        self.tab_2_show_table_room.setText(_translate("Dialog", "Вивести данні всіх знижок"))
        self.tab_2_update_room_butt.setText(_translate("Dialog", "Змінити данні"))
        self.label_12.setText(_translate("Dialog", "Номер кімнати:"))
        self.tab_2_delete_room_butt.setText(_translate("Dialog", "Видалити кімнату"))
        self.tab_2_get_room_butt.setText(_translate("Dialog", "Отримати данні кімнати"))
        self.label_13.setText(_translate("Dialog", "Номер кімнати:"))
        self.label_14.setText(_translate("Dialog", "Місткість кімнати:"))
        self.label_15.setText(_translate("Dialog", "Комфорт кімнати:"))
        self.label_16.setText(_translate("Dialog", "Ціна кімнати:"))
        self.tab_2_create_room_butt.setText(_translate("Dialog", "Сворити"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Список номерів"))
        self.tab_3_show_table_dis_butt.setText(_translate("Dialog", "Вивести данні всіх знижок"))
        self.tab_3_update_dis_butt.setText(_translate("Dialog", "Змінити данні"))
        self.label_17.setText(_translate("Dialog", "Назва знижки:"))
        self.label_18.setText(_translate("Dialog", "Відсоток:"))
        self.tab_3_get_dis_butt.setText(_translate("Dialog", "Отримати данні знижки"))
        self.tab_3_create_dis_butt.setText(_translate("Dialog", "Сворити"))
        self.label_19.setText(_translate("Dialog", "Назва нової знижки:"))
        self.tab_3_delete_butt.setText(_translate("Dialog", "Видалити знижку"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Список знижок"))
        self.label_20.setText(_translate("Dialog", "id"))
        self.tab_4_show_table_res_butt.setText(_translate("Dialog", "Вивести список бронювань"))
        self.tab_4_delete_res_butt.setText(_translate("Dialog", "Видалити"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Список бронюваннь"))
        self.tab_5_show_table_order_butt.setText(_translate("Dialog", "Вивести список бронювань"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Список замовленнь"))
        self.tab_6_show_table_settlement_butt.setText(_translate("Dialog", "Вивести список заселень"))
        self.label_21.setText(_translate("Dialog", "Номер паспорту:"))
        self.tab_6_on_sett_butt.setText(_translate("Dialog", "Відкрити"))
        self.label_22.setText(_translate("Dialog", "Відкрити заселення :"))
        self.label_23.setText(_translate("Dialog", "Номер кімнати:"))
        self.label_24.setText(_translate("Dialog", "Дата в\'їзду"))
        self.label_26.setText(_translate("Dialog", "Номер паспорту:"))
        self.label_27.setText(_translate("Dialog", "Номер кімнати:"))
        self.tab_6_close_sett_butt.setText(_translate("Dialog", "Закрити"))
        self.label_28.setText(_translate("Dialog", "Закрити заселення :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Dialog", "Список заселень"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Admin_win()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
