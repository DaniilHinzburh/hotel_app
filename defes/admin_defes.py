import init_django_orm  # noqa: F401
from PyQt5 import QtWidgets
from datetime import date, timedelta, datetime
from db.models import Room, Reservation, Discount, User
from defes.general_defes import count_total_price, apply_discounts
from Windows.admin_win import Admin_win
from defes import general_defes



