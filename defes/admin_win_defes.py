from django.db.models import F
from defes import general_defes, win_defes, admin_defes
from db.models import Room, Reservation, Discount, User, Order, Settlement
from decimal import Decimal
from datetime import datetime


def tab_1_show_table_user(self):
    queryset = User.objects.filter().values("id", "first_name", "last_name", "phone", "password", "passport",
                                            "address",
                                            "comment")
    general_defes.fill_table_widget_with_data(queryset, self.table_user)


def tab_1_get_user_butt_clicked(self):
    self.user = admin_defes.get_user_by_passport(self.tab_1_passport_in.text())
    self.tab_1_first_name.setText(self.user.first_name)
    self.tab_1_last_name.setText(self.user.last_name)
    self.tab_1_password.setText(self.user.password)
    self.tab_1_phone.setText(self.user.phone)
    self.tab_1_adress.setText(self.user.address)
    self.tab_1_comment.setText(self.user.comment)
    general_defes.fill_table_widget_with_data(general_defes.get_user_discounts(self.user), self.table_user_dis)
    self.tab_1_update_user_butt.setEnabled(True)
    self.tab_1_delete_user_dutt.setEnabled(True)
    win_defes.beack_to_normal_butt_admin(self.tab_1_delete_user_dutt)
    win_defes.beack_to_normal_butt_admin(self.tab_1_update_user_butt)
    win_defes.beack_to_normal_butt_admin(self.tab_1_dell_dis_butt)
    win_defes.beack_to_normal_butt_admin(self.tab_1_add_dis_butt)


def tab_1_update_user_butt_clicked(self):
    win_defes.green_butt_admin(self.tab_1_update_user_butt)
    self.user.first_name = self.tab_1_first_name.text()
    self.user.last_name = self.tab_1_last_name.text()
    self.user.password = self.tab_1_password.text()
    self.user.phone = self.tab_1_phone.text()
    self.user.address = self.tab_1_adress.text()
    self.user.comment = self.tab_1_comment.text()
    self.user.save()


def tab_1_delete_user_butt_clicked(self):
    self.user.delete()
    self.tab_1_first_name.setText("")
    self.tab_1_last_name.setText("")
    self.tab_1_password.setText("")
    self.tab_1_phone.setText("")
    self.tab_1_adress.setText("")
    self.tab_1_comment.setText("")
    win_defes.green_butt_admin(self.tab_1_delete_user_dutt)


def tab_1_dell_dis_butt_clicked(self):
    admin_defes.delete_user_disc(self.user, self.tab_1_dis_name.text())
    win_defes.green_butt_admin(self.tab_1_dell_dis_butt)


def tab_1_add_dis_butt_clicked(self):
    admin_defes.add_discount_to_user(self.user, self.tab_1_dis_name.text())
    win_defes.green_butt_admin(self.tab_1_add_dis_butt)


# методы tab_2
def tab_2_show_table_room_clicked(self):
    queryset = Room.objects.filter().annotate(passport=F("user__passport")).values("number", "capacity", "comfort",
                                                                                   "price", "is_free",
                                                                                   "passport")

    general_defes.fill_table_widget_with_data(queryset, self.table_room)


def tab_2_get_room_butt_clicked(self):
    try:
        self.room = Room.objects.get(number=int(self.tab_2_number_in.text()))
        win_defes.beack_to_normal_butt_admin(self.tab_2_delete_room_butt)
        win_defes.beack_to_normal_butt_admin(self.tab_2_update_room_butt)
        win_defes.beack_to_normal_butt_admin(self.tab_2_create_room_butt)
        self.tab_2_capacity.setText(str(self.room.capacity))
        self.tab_2_comfort.setText(str(self.room.comfort))
        self.tab_2_price.setText(str(self.room.price))
    except Exception as e:
        print(e)


def tab_2_delete_room_butt_clicked(self):
    try:
        self.room.delete()
        win_defes.green_butt_admin(self.tab_2_delete_room_butt)
    except Exception as e:
        print(e)


def tab_2_update_room_butt_clicked(self):
    try:
        self.room.capacity = int(self.tab_2_capacity.text())
        self.room.comfort = self.tab_2_comfort.text()
        self.room.price = int(self.tab_2_price.text())
        win_defes.green_butt_admin(self.tab_2_update_room_butt)
        self.room.save()
    except Exception as e:
        print(e)


def tab_2_create_room_butt_clicked(self):
    try:
        win_defes.green_butt_admin(self.tab_2_create_room_butt)
        new_room = Room(
            number=int(self.tab_2_number_new_room.text()),
            capacity=int(self.tab_2_capacity_new_room.text()),
            comfort=self.tab_2_comfort_new_room.text(),
            price=int(self.tab_2_price_new_room.text())
        )
        new_room.save()
    except Exception as e:
        print(e)


# методы tab_3
def tab_3_show_table_dis_butt_clicked(self):
    queryset = Discount.objects.filter().values("name", "percent")
    general_defes.fill_table_widget_with_data(queryset, self.table_dis)
    win_defes.beack_to_normal_butt_admin(self.tab_3_create_dis_butt)


def tab_3_get_dis_butt_clicked(self):
    try:
        self.discount = Discount.objects.get(name=str(self.tab_3_name_dis.text()))
        self.tab_3_name_dis_2.setText(self.discount.name)
        self.tab_3_percent_dis.setText(str(self.discount.percent))
        win_defes.beack_to_normal_butt_admin(self.tab_3_update_dis_butt)
        win_defes.beack_to_normal_butt_admin(self.tab_3_delete_butt)
    except Exception as e:
        print(e)


def tab_3_delete_butt_clicked(self):
    try:
        self.discount.delete()
        win_defes.green_butt_admin(self.tab_3_delete_butt)
    except Exception as e:
        print(e)


def tab_3_update_dis_butt_clicked(self):
    try:
        self.discount.name = self.tab_3_name_dis_2.text()
        self.discount.percent = Decimal(self.tab_3_percent_dis.text())
        win_defes.green_butt_admin(self.tab_3_update_dis_butt)
        self.discount.save()
    except Exception as e:
        print(e)


def tab_3_create_dis_butt_clicked(self):
    try:
        new_dis = Discount(
            name=self.tab_3_name_new_dis.text(),
            percent=Decimal(self.tab_3_percent_new_dis.text())
        )
        new_dis.save()
        win_defes.green_butt_admin(self.tab_3_create_dis_butt)
    except Exception as e:
        print(e)


# методы tab_4
def tab_4_show_table_res_butt_clicked(self):
    win_defes.beack_to_normal_butt_admin(self.tab_4_delete_res_butt)
    self.tab_4_id_res.setText("")
    queryset = Reservation.objects.filter().annotate(passport=F("user__passport")).values("id", "passport",
                                                                                          "room__number",
                                                                                          "check_in_date",
                                                                                          "check_out_date")
    general_defes.fill_table_widget_with_data(queryset, self.table_res)


def tab_4_delete_res_butt_clicked(self):
    try:
        reservation = Reservation.objects.get(id=int(self.tab_4_id_res.text()))
        reservation.delete()
        win_defes.green_butt_admin(self.tab_4_delete_res_butt)
    except Exception as e:
        print(e)


# методы tab_5
def tab_5_show_table_order_butt_clicked(self):
    queryset = Order.objects.filter().annotate(passport=F("user__passport")).values("id", "passport", "room__number",
                                                                                    "check_in_date",
                                                                                    "check_out_date", "price")
    general_defes.fill_table_widget_with_data(queryset, self.table_order)


# методы tab_6
def tab_6_show_table_settlement_butt_clicked(self):
    queryset = Settlement.objects.filter().annotate(passport=F("user__passport")).values("passport", "room__number",
                                                                                         "check_in_date",
                                                                                         "check_out_date")
    general_defes.fill_table_widget_with_data(queryset, self.table_settlement)


def tab_6_on_sett_butt_clicked(self):
    try:
        settlement = Settlement(
            user=admin_defes.get_user_by_passport(self.tab_6_passport_on_sett.text()),
            room=Room.objects.get(number=int(self.tab_6_room_num_on_sett.text())),
            check_in_date=datetime.strptime(self.tab_6_data_in.text(), "%Y-%m-%d").date()
        )
        settlement.save()
        win_defes.green_butt_admin(self.tab_6_on_sett_butt)
        room = Room.objects.get(int(self.tab_6_room_num_on_sett.text()))
        room.is_free = False
    except Exception as e:
        print(e)


def tab_6_close_sett_butt_clicked(self):
    try:
        win_defes.green_butt_admin(self.tab_6_close_sett_butt)
        settlement = Settlement.objects.get(user__passport=self.tab_6_passport_close_sett.text(),
                                            room__number=int(self.tab_6_room_num_close_sett.text()))
        settlement.check_out_date = datetime.now().date()
        settlement.save()
        Reservation.objects.filter(room__number=int(self.tab_6_room_num_close_sett.text()),
                                   check_in_date=settlement.check_in_date).delete()
        room = Room.objects.get(int(self.tab_6_room_num_on_sett.text()))
        room.is_free = True
    except Exception as e:
        print(e)
