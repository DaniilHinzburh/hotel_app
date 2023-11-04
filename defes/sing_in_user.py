import sys
import init_django_orm  # noqa: F401
from db.models import User


def create_user(first_name: str, last_name: str, phone: int, passport: int, address: str = None, comment: str = None):
    try:
        user = User(first_name=first_name, last_name=last_name, phone=phone, passport=passport, address=address,
                    comment=comment)
        user.save()
        return True
    except Exception:
        return False


def user_found(phone_number):
    if phone_number == "":
        return None
    try:
        user = User.objects.get(phone=phone_number)
        return user
    except User.DoesNotExist:
        return None
