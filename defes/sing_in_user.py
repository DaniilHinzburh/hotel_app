import init_django_orm  # noqa: F401
from db.models import User


def create_user(
        first_name: str,
        last_name: str,
        phone: int,
        password: str,
        passport: str,
        address: str = None,
        comment: str = None):
    try:
        user = User(first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    password=password,
                    passport=passport,
                    address=address,
                    comment=comment)
        user.save()
        return True
    except Exception as e:
        print(e)
        return False


def user_found(phone_number, password):
    if phone_number == "":
        return None
    try:
        user = User.objects.get(phone=phone_number)
        if user.password == password:
            return user
        else:
            return None
    except User.DoesNotExist:
        return None
