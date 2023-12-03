import init_django_orm  # noqa: F401


def click_butt(self, set, elem, but_click, append, but_1, but_2):
    set[elem] = append
    but_click.setStyleSheet("QPushButton {\n"
                            "    color: DarkBlue;\n"
                            "    border: 3px solid bleak;\n"
                            "    border-radius: 20px;\n"
                            "    background-color: green;\n"
                            "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                            "    padding: 0; /* Удаление внутренних отступов */\n"
                            "}\n"
                            "\n"

                            "\n"
                            "")
    but_1.setStyleSheet("QPushButton {\n"
                        "    color: DarkBlue;\n"
                        "    border: 3px solid bleak;\n"
                        "    border-radius: 20px;\n"
                        "    background-color: grey;\n"
                        "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                        "    padding: 0; /* Удаление внутренних отступов */\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "    background-color: white;\n"
                        "}\n"
                        "\n"
                        "")
    but_2.setStyleSheet("QPushButton {\n"
                        "    color: DarkBlue;\n"
                        "    border: 3px solid bleak;\n"
                        "    border-radius: 20px;\n"
                        "    background-color: grey;\n"
                        "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                        "    padding: 0; /* Удаление внутренних отступов */\n"
                        "}\n"
                        "\n"
                        "QPushButton:hover {\n"
                        "    background-color: white;\n"
                        "}\n"
                        "\n"
                        "")


def green_butt(butt):
    butt.setEnabled(False)
    butt.setText("Оформлено!")
    butt.setStyleSheet("QPushButton {\n"
                       "    color: DarkBlue;\n"
                       "    border: 3px solid bleak;\n"
                       "    border-radius: 20px;\n"
                       "    background-color: green;\n"
                       "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                       "    padding: 0; /* Удаление внутренних отступов */\n"
                       "}\n"
                       "\n"

                       "\n"
                       "")


def green_butt_admin(butt):
    butt.setEnabled(False)
    butt.setStyleSheet("QPushButton {\n"
                       "    color: DarkBlue;\n"
                       "    border: 3px solid bleak;\n"
                       "    border-radius: 20px;\n"
                       "    background-color: green;\n"
                       "    text-align: center; /* Выравнивание текста по центру по вертикали */\n"
                       "    padding: 0; /* Удаление внутренних отступов */\n"
                       "}\n"
                       "\n"

                       "\n"
                       "")


def beack_to_normal_butt_admin(butt):
    butt.setEnabled(True)
    butt.setStyleSheet("QPushButton {\n"
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
