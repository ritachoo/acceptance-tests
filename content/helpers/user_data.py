from __future__ import annotations

from faker import Faker


def generate_user_data() -> UserData:
    user_data = UserData()
    data_generator = Faker()

    user_data.set_name(data_generator.name())
    user_data.set_email(data_generator.email())
    user_data.set_password(data_generator.password(special_chars=False))
    return user_data


class UserData:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__password = None

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    def set_name(self, name: str) -> UserData:
        self.__name = name
        return self

    def set_email(self, email: str) -> UserData:
        self.__email = email
        return self

    def set_password(self, password: str) -> UserData:
        self.__password = password
        return self
