import init_django_orm  # noqa: F401
import db.models

from PyQt5 import QtCore, QtGui, QtWidgets
from defes import user_defes, general_defes
from defes.user_win_defes import click_butt
from datetime import date, timedelta, datetime


class User_Win(object):
    user = None
    tab_1_set = [None, None, None, None, None]
    tab_2_set = [None, None, None]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1001, 1001))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.err_label = QtWidgets.QLabel(self.centralwidget)
        self.err_label.setGeometry(QtCore.QRect(10, 400, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.err_label.setFont(font)
        self.err_label.setStyleSheet("color: rgb(231, 0, 0);")
        self.err_label.setText("")
        self.err_label.setAlignment(QtCore.Qt.AlignCenter)
        self.err_label.setObjectName("err_label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 780, 770))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
                                     "    color: DarkBlue;\n"
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
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("QPushButton {\n"
                                 "    color: DarkBlue;\n"
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
        self.tab_1.setObjectName("tab_1")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 791, 731))
        self.label_6.setStyleSheet("alignment: center;\n"
                                   "    QLabel {\n"
                                   "        color: DarkBlue;\n"
                                   "        border: 3px solid bleak;\n"
                                   "        border-radius: 20px;\n"
                                   "        background-color: rgb(238, 238, 238);\n"
                                   "        padding: 10px; /* Удаление внутренних отступов */\n"
                                   "    }")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.create_order_butt_3 = QtWidgets.QPushButton(self.tab_1)
        self.create_order_butt_3.setGeometry(QtCore.QRect(220, 630, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_order_butt_3.setFont(font)
        self.create_order_butt_3.setStyleSheet("QPushButton {\n"
                                               "    color: DarkBlue;\n"
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
                                               "\n"
                                               "")
        self.create_order_butt_3.setObjectName("create_order_butt_3")
        self.label_21 = QtWidgets.QLabel(self.tab_1)
        self.label_21.setGeometry(QtCore.QRect(350, 270, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_1)
        self.label_22.setGeometry(QtCore.QRect(20, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.tab_1_6_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_6_butt.setGeometry(QtCore.QRect(630, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_6_butt.setFont(font)
        self.tab_1_6_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_1_6_butt.setObjectName("tab_1_6_butt")
        self.tab_1_stand_but = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_stand_but.setGeometry(QtCore.QRect(350, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_stand_but.setFont(font)
        self.tab_1_stand_but.setStyleSheet("QPushButton {\n"
                                           "    color: DarkBlue;\n"
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
                                           "\n"
                                           "")
        self.tab_1_stand_but.setObjectName("tab_1_stand_but")
        self.tab_1_lux_but = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_lux_but.setGeometry(QtCore.QRect(630, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_lux_but.setFont(font)
        self.tab_1_lux_but.setStyleSheet("QPushButton {\n"
                                         "    color: DarkBlue;\n"
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
                                         "\n"
                                         "")
        self.tab_1_lux_but.setObjectName("tab_1_lux_but")
        self.count_price_butt_3 = QtWidgets.QPushButton(self.tab_1)
        self.count_price_butt_3.setGeometry(QtCore.QRect(20, 550, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_price_butt_3.setFont(font)
        self.count_price_butt_3.setStyleSheet("QPushButton {\n"
                                              "    color: DarkBlue;\n"
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
                                              "\n"
                                              "")
        self.count_price_butt_3.setObjectName("count_price_butt_3")
        self.tab_1_2_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_2_butt.setGeometry(QtCore.QRect(350, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_2_butt.setFont(font)
        self.tab_1_2_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_1_2_butt.setObjectName("tab_1_2_butt")
        self.tab_1_pilux_but = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_pilux_but.setGeometry(QtCore.QRect(490, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_pilux_but.setFont(font)
        self.tab_1_pilux_but.setStyleSheet("QPushButton {\n"
                                           "    color: DarkBlue;\n"
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
                                           "\n"
                                           "")
        self.tab_1_pilux_but.setObjectName("tab_1_pilux_but")
        self.label_23 = QtWidgets.QLabel(self.tab_1)
        self.label_23.setGeometry(QtCore.QRect(20, 70, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.price_text_3 = QtWidgets.QLabel(self.tab_1)
        self.price_text_3.setGeometry(QtCore.QRect(350, 550, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.price_text_3.setFont(font)
        self.price_text_3.setStyleSheet("color: DarkBlue ;\n"
                                        "border: 3px solid bleak;\n"
                                        "border-radius: 20px;\n"
                                        "background-color: rgb(238, 238, 238);")
        self.price_text_3.setText("")
        self.price_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.price_text_3.setObjectName("price_text_3")
        self.tab_1_4_butt = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_4_butt.setGeometry(QtCore.QRect(490, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_4_butt.setFont(font)
        self.tab_1_4_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_1_4_butt.setObjectName("tab_1_4_butt")
        self.number_text_3 = QtWidgets.QLineEdit(self.tab_1)
        self.number_text_3.setGeometry(QtCore.QRect(520, 270, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.number_text_3.setFont(font)
        self.number_text_3.setStyleSheet("color: DarkBlue ;\n"
                                         "border: 3px solid bleak;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: rgb(238, 238, 238);")
        self.number_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.number_text_3.setObjectName("number_text_3")
        self.tab_1_show_rooms = QtWidgets.QPushButton(self.tab_1)
        self.tab_1_show_rooms.setGeometry(QtCore.QRect(20, 270, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_1_show_rooms.setFont(font)
        self.tab_1_show_rooms.setStyleSheet("QPushButton {\n"
                                            "    color: DarkBlue;\n"
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
                                            "\n"
                                            "")
        self.tab_1_show_rooms.setObjectName("tab_1_show_rooms")
        self.label_25 = QtWidgets.QLabel(self.tab_1)
        self.label_25.setGeometry(QtCore.QRect(20, 130, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_1)
        self.label_26.setGeometry(QtCore.QRect(20, 200, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.data_in_text = QtWidgets.QLineEdit(self.tab_1)
        self.data_in_text.setGeometry(QtCore.QRect(350, 130, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.data_in_text.setFont(font)
        self.data_in_text.setStyleSheet("color: DarkBlue ;\n"
                                        "border: 3px solid bleak;\n"
                                        "border-radius: 20px;\n"
                                        "background-color: rgb(238, 238, 238);")
        self.data_in_text.setAlignment(QtCore.Qt.AlignCenter)
        self.data_in_text.setObjectName("data_in_text")
        self.data_out_text = QtWidgets.QLineEdit(self.tab_1)
        self.data_out_text.setGeometry(QtCore.QRect(350, 200, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.data_out_text.setFont(font)
        self.data_out_text.setStyleSheet("color: DarkBlue ;\n"
                                         "border: 3px solid bleak;\n"
                                         "border-radius: 20px;\n"
                                         "background-color: rgb(238, 238, 238);")
        self.data_out_text.setAlignment(QtCore.Qt.AlignCenter)
        self.data_out_text.setObjectName("data_out_text")
        self.do_discounts_2 = QtWidgets.QPushButton(self.tab_1)
        self.do_discounts_2.setGeometry(QtCore.QRect(20, 490, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.do_discounts_2.setFont(font)
        self.do_discounts_2.setStyleSheet("QPushButton {\n"
                                          "    color: DarkBlue;\n"
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
                                          "\n"
                                          "")
        self.do_discounts_2.setObjectName("do_discounts_2")
        self.table_1 = QtWidgets.QTableWidget(self.tab_1)
        self.table_1.setGeometry(QtCore.QRect(82, 330, 618, 150))
        self.table_1.setObjectName("table_1")
        self.table_1.setColumnCount(0)
        self.table_1.setRowCount(0)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 791, 731))
        self.label_4.setStyleSheet("alignment: center;\n"
                                   "    QLabel {\n"
                                   "        color: DarkBlue;\n"
                                   "        border: 3px solid bleak;\n"
                                   "        border-radius: 20px;\n"
                                   "        background-color: rgb(238, 238, 238);\n"
                                   "        padding: 10px; /* Удаление внутренних отступов */\n"
                                   "    }")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: DarkBlue ;\n"
                                   "border: 3px solid bleak;\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(238, 238, 238);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: DarkBlue ;\n"
                                   "border: 3px solid bleak;\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(238, 238, 238);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.tab_2_stand_but = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_stand_but.setGeometry(QtCore.QRect(350, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_stand_but.setFont(font)
        self.tab_2_stand_but.setStyleSheet("QPushButton {\n"
                                           "    color: DarkBlue;\n"
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
                                           "\n"
                                           "")
        self.tab_2_stand_but.setObjectName("stand_but")
        self.tab_2_pilux_but = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_pilux_but.setGeometry(QtCore.QRect(490, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_pilux_but.setFont(font)
        self.tab_2_pilux_but.setStyleSheet("QPushButton {\n"
                                           "    color: DarkBlue;\n"
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
                                           "\n"
                                           "")
        self.tab_2_pilux_but.setObjectName("pilux_but")
        self.tab_2_lux_but = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_lux_but.setGeometry(QtCore.QRect(630, 10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_lux_but.setFont(font)
        self.tab_2_lux_but.setStyleSheet("QPushButton {\n"
                                         "    color: DarkBlue;\n"
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
                                         "\n"
                                         "")
        self.tab_2_lux_but.setObjectName("lux_but")
        self.tab_2_2_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_2_butt.setGeometry(QtCore.QRect(350, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_2_butt.setFont(font)
        self.tab_2_2_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_2_2_butt.setObjectName("_2_butt")
        self.tab_2_6_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_6_butt.setGeometry(QtCore.QRect(630, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_6_butt.setFont(font)
        self.tab_2_6_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_2_6_butt.setObjectName("_6_butt")
        self.tab_2_4_butt = QtWidgets.QPushButton(self.tab_3)
        self.tab_2_4_butt.setGeometry(QtCore.QRect(490, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tab_2_4_butt.setFont(font)
        self.tab_2_4_butt.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.tab_2_4_butt.setObjectName("_4_butt")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 490, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.number_text = QtWidgets.QLineEdit(self.tab_3)
        self.number_text.setGeometry(QtCore.QRect(190, 490, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.number_text.setFont(font)
        self.number_text.setStyleSheet("color: DarkBlue ;\n"
                                       "border: 3px solid bleak;\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(238, 238, 238);")
        self.number_text.setAlignment(QtCore.Qt.AlignCenter)
        self.number_text.setObjectName("number_text")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 190, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.days_count = QtWidgets.QLineEdit(self.tab_3)
        self.days_count.setGeometry(QtCore.QRect(270, 190, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.days_count.setFont(font)
        self.days_count.setStyleSheet("color: DarkBlue ;\n"
                                      "border: 3px solid bleak;\n"
                                      "border-radius: 20px;\n"
                                      "background-color: rgb(238, 238, 238);")
        self.days_count.setAlignment(QtCore.Qt.AlignCenter)
        self.days_count.setObjectName("days_count")
        self.price_text = QtWidgets.QLabel(self.tab_3)
        self.price_text.setGeometry(QtCore.QRect(350, 550, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.price_text.setFont(font)
        self.price_text.setStyleSheet("color: DarkBlue ;\n"
                                      "border: 3px solid bleak;\n"
                                      "border-radius: 20px;\n"
                                      "background-color: rgb(238, 238, 238);")
        self.price_text.setText("")
        self.price_text.setAlignment(QtCore.Qt.AlignCenter)
        self.price_text.setObjectName("price_text")
        self.count_price_butt = QtWidgets.QPushButton(self.tab_3)
        self.count_price_butt.setGeometry(QtCore.QRect(20, 550, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.count_price_butt.setFont(font)
        self.count_price_butt.setStyleSheet("QPushButton {\n"
                                            "    color: DarkBlue;\n"
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
                                            "\n"
                                            "")
        self.count_price_butt.setObjectName("count_price_butt")
        self.create_order_butt = QtWidgets.QPushButton(self.tab_3)
        self.create_order_butt.setGeometry(QtCore.QRect(220, 630, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_order_butt.setFont(font)
        self.create_order_butt.setStyleSheet("QPushButton {\n"
                                             "    color: DarkBlue;\n"
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
                                             "\n"
                                             "")
        self.create_order_butt.setObjectName("create_order_butt")
        self.show_rooms = QtWidgets.QPushButton(self.tab_3)
        self.show_rooms.setGeometry(QtCore.QRect(430, 190, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_rooms.setFont(font)
        self.show_rooms.setStyleSheet("QPushButton {\n"
                                      "    color: DarkBlue;\n"
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
                                      "\n"
                                      "")
        self.show_rooms.setObjectName("show_rooms")
        self.do_discounts = QtWidgets.QPushButton(self.tab_3)
        self.do_discounts.setGeometry(QtCore.QRect(350, 490, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.do_discounts.setFont(font)
        self.do_discounts.setStyleSheet("QPushButton {\n"
                                        "    color: DarkBlue;\n"
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
                                        "\n"
                                        "")
        self.do_discounts.setObjectName("do_discounts")
        self.table_2 = QtWidgets.QTableWidget(self.tab_3)
        self.table_2.setGeometry(QtCore.QRect(82, 250, 618, 231))
        self.table_2.setObjectName("table_2")
        self.table_2.setColumnCount(0)
        self.table_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 790, 730))
        self.label_7.setStyleSheet("alignment: center;\n"
                                   "    QLabel {\n"
                                   "        color: DarkBlue;\n"
                                   "        border: 3px solid bleak;\n"
                                   "        border-radius: 20px;\n"
                                   "        background-color: rgb(238, 238, 238);\n"
                                   "        padding: 10px; /* Удаление внутренних отступов */\n"
                                   "    }")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 390, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: DarkBlue ;\n"
                                    "border: 3px solid bleak;\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(238, 238, 238);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.delete_reservation_butt = QtWidgets.QPushButton(self.tab_2)
        self.delete_reservation_butt.setGeometry(QtCore.QRect(230, 610, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_reservation_butt.setFont(font)
        self.delete_reservation_butt.setStyleSheet("QPushButton {\n"
                                                   "    color: DarkBlue;\n"
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
                                                   "\n"
                                                   "")
        self.delete_reservation_butt.setObjectName("delete_reservation_butt")
        self.id_res_text = QtWidgets.QLineEdit(self.tab_2)
        self.id_res_text.setGeometry(QtCore.QRect(360, 390, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.id_res_text.setFont(font)
        self.id_res_text.setStyleSheet("color: DarkBlue ;\n"
                                       "border: 3px solid bleak;\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(238, 238, 238);")
        self.id_res_text.setAlignment(QtCore.Qt.AlignCenter)
        self.id_res_text.setObjectName("id_res_text")
        self.show_my_res = QtWidgets.QPushButton(self.tab_2)
        self.show_my_res.setGeometry(QtCore.QRect(10, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_my_res.setFont(font)
        self.show_my_res.setStyleSheet("QPushButton {\n"
                                       "    color: DarkBlue;\n"
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
                                       "\n"
                                       "")
        self.show_my_res.setObjectName("show_my_res")
        self.table_3 = QtWidgets.QTableWidget(self.tab_2)
        self.table_3.setGeometry(QtCore.QRect(30, 100, 711, 271))
        self.table_3.setObjectName("table_3")
        self.table_3.setColumnCount(0)
        self.table_3.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 791, 731))
        self.label_5.setStyleSheet("alignment: center;\n"
                                   "    QLabel {\n"
                                   "        color: DarkBlue;\n"
                                   "        border: 3px solid bleak;\n"
                                   "        border-radius: 20px;\n"
                                   "        background-color: rgb(238, 238, 238);\n"
                                   "        padding: 10px; /* Удаление внутренних отступов */\n"
                                   "    }")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/resep.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.show_my_disc_butt = QtWidgets.QPushButton(self.tab)
        self.show_my_disc_butt.setGeometry(QtCore.QRect(10, 10, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.show_my_disc_butt.setFont(font)
        self.show_my_disc_butt.setStyleSheet("QPushButton {\n"
                                             "    color: DarkBlue;\n"
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
                                             "\n"
                                             "")
        self.show_my_disc_butt.setObjectName("show_my_disc_butt")
        self.table_4 = QtWidgets.QTableWidget(self.tab)
        self.table_4.setGeometry(QtCore.QRect(30, 80, 711, 271))
        self.table_4.setObjectName("table_4")
        self.table_4.setColumnCount(0)
        self.table_4.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # кнопки tab_1
        self.tab_1_stand_but.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 0, self.tab_1_stand_but, "standard", self.tab_1_pilux_but,
                               self.tab_1_lux_but)

        )
        self.tab_1_pilux_but.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 0, self.tab_1_pilux_but, "deluxe", self.tab_1_stand_but,
                               self.tab_1_lux_but)
        )
        self.tab_1_lux_but.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 0, self.tab_1_lux_but, "suite", self.tab_1_stand_but,
                               self.tab_1_pilux_but)
        )
        self.tab_1_2_butt.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 1, self.tab_1_2_butt, 2, self.tab_1_4_butt, self.tab_1_6_butt)
        )
        self.tab_1_4_butt.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 1, self.tab_1_4_butt, 4, self.tab_1_2_butt, self.tab_1_6_butt)
        )
        self.tab_1_6_butt.clicked.connect(
            lambda: click_butt(self, self.tab_1_set, 1, self.tab_1_6_butt, 6, self.tab_1_2_butt, self.tab_1_4_butt)
        )
        self.tab_1_show_rooms.clicked.connect(lambda: self.tab_1_show_rooms_def())

        # кнопки tab_2
        self.tab_2_stand_but.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 0, self.tab_2_stand_but, "standard", self.tab_2_pilux_but,
                               self.tab_2_lux_but)
        )
        self.tab_2_pilux_but.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 0, self.tab_2_pilux_but, "deluxe", self.tab_2_stand_but,
                               self.tab_2_lux_but)
        )
        self.tab_2_lux_but.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 0, self.tab_2_lux_but, "suite", self.tab_2_stand_but,
                               self.tab_2_pilux_but)
        )
        self.tab_2_2_butt.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 1, self.tab_2_2_butt, 2, self.tab_2_4_butt, self.tab_2_6_butt)
        )
        self.tab_2_4_butt.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 1, self.tab_2_4_butt, 4, self.tab_2_2_butt, self.tab_2_6_butt)
        )
        self.tab_2_6_butt.clicked.connect(
            lambda: click_butt(self, self.tab_2_set, 1, self.tab_2_6_butt, 6, self.tab_2_2_butt, self.tab_2_4_butt)
        )
        self.show_rooms.clicked.connect(lambda: self.tab_2_show_rooms_def())

    # методы
    def tab_1_show_rooms_def(self):
        try:
            self.tab_1_set[3] = datetime.strptime(self.data_in_text.text(), "%Y-%m-%d").date()
            self.tab_1_set[4] = datetime.strptime(self.data_out_text.text(), "%Y-%m-%d").date()
            data = user_defes.find_available_rooms(*self.tab_1_set)
            general_defes.fill_table_widget_with_data(data, self.table_1)
        except Exception as e:
            print(e)

    def tab_2_show_rooms_def(self):
        try:
            self.tab_2_set[2] = int(self.days_count.text())
            data = user_defes.find_available_rooms(*self.tab_2_set)
            general_defes.fill_table_widget_with_data(data, self.table_2)
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_order_butt_3.setText(_translate("MainWindow", "Оформити"))
        self.label_21.setText(_translate("MainWindow", "Оберіть номер"))
        self.label_22.setText(_translate("MainWindow", "Оберіть категорію"))
        self.tab_1_6_butt.setText(_translate("MainWindow", "6"))
        self.tab_1_stand_but.setText(_translate("MainWindow", "Стандарт"))
        self.tab_1_lux_but.setText(_translate("MainWindow", "Люкс"))
        self.count_price_butt_3.setText(_translate("MainWindow", "Розрахувати кінцеву ціну:"))
        self.tab_1_2_butt.setText(_translate("MainWindow", "2"))
        self.tab_1_pilux_but.setText(_translate("MainWindow", "Напівлюкс"))
        self.label_23.setText(_translate("MainWindow", "Оберіть місткість"))
        self.tab_1_4_butt.setText(_translate("MainWindow", "4"))
        self.tab_1_show_rooms.setText(_translate("MainWindow", "Підібрати номери"))
        self.label_25.setText(_translate("MainWindow", "Вкажіть дату заселення"))
        self.label_26.setText(_translate("MainWindow", "Вкажіть дату виселення"))
        self.do_discounts_2.setText(_translate("MainWindow", "Застосувати знижки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Забронювати номер"))
        self.label_2.setText(_translate("MainWindow", "Оберіть категорію"))
        self.label_9.setText(_translate("MainWindow", "Оберіть місткість"))
        self.tab_2_stand_but.setText(_translate("MainWindow", "Стандарт"))
        self.tab_2_pilux_but.setText(_translate("MainWindow", "Напівлюкс"))
        self.tab_2_lux_but.setText(_translate("MainWindow", "Люкс"))
        self.tab_2_2_butt.setText(_translate("MainWindow", "2"))
        self.tab_2_6_butt.setText(_translate("MainWindow", "6"))
        self.tab_2_4_butt.setText(_translate("MainWindow", "4"))
        self.label_11.setText(_translate("MainWindow", "Оберіть номер"))
        self.label_12.setText(_translate("MainWindow", "Оберіть кількість ночей"))
        self.count_price_butt.setText(_translate("MainWindow", "Розрахувати кінцеву ціну:"))
        self.create_order_butt.setText(_translate("MainWindow", "Оформити"))
        self.show_rooms.setText(_translate("MainWindow", "Підібрати номери"))
        self.do_discounts.setText(_translate("MainWindow", "Застосувати знижки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Зняти номер"))
        self.label_20.setText(_translate("MainWindow", "Вкажіть id замолення"))
        self.delete_reservation_butt.setText(_translate("MainWindow", "Видалити"))
        self.show_my_res.setText(_translate("MainWindow", "Показати мої бронювання"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Мої бронювання"))
        self.show_my_disc_butt.setText(_translate("MainWindow", "Показати мої знижки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Знижки"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = User_Win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
