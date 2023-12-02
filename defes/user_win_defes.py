import init_django_orm  # noqa: F401
from defes import user_defes, general_defes
from defes.win_defes import green_butt
from datetime import timedelta, datetime
from decimal import Decimal


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


def tab_1_create_order_click(self):
    green_butt(self.create_order_butt_3)
    user_defes.create_reservation(
        self.user,
        int(self.number_text_3.text()),
        datetime.strptime(self.data_in_text.text(), "%Y-%m-%d").date(),
        datetime.strptime(self.data_out_text.text(), "%Y-%m-%d").date(),
        Decimal(self.price_text_3.text()))


def tab_2_create_order_click(self):
    green_butt(self.create_order_butt)
    user_defes.create_reservation(
        self.user,
        int(self.number_text.text()),
        datetime.now().date(),
        datetime.now().date() + timedelta(days=int(self.days_count.text())),
        Decimal(self.price_text.text()))


def tab_3_show_reservation(self):
    general_defes.fill_table_widget_with_data(user_defes.get_reservation(self.user), self.table_3)


def tab_3_delete_reservation(self):
    if self.id_res_text.text() != "":
        user_defes.delete_reservation(int(self.id_res_text.text()))
        self.id_res_text.setText("")


def tab_4_show_discount(self):
    general_defes.fill_table_widget_with_data(user_defes.show_my_discount(self.user), self.table_4)
