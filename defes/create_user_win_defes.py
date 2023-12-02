from defes import sing_in_user


def create_user(self):
    user_list = [
        self.first_name_text.text(),
        self.last_name_text.text(),
        self.phone_text_.text(),
        self.password_text.text(),
        self.passport_text.text(),
        self.adress_text.text()

    ]

    if sing_in_user.create_user(*user_list):
        self.create_butt.setEnabled(False)
        self.create_butt.setText("Створено!")
