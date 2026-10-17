from tools.validation import *


class Member:
    MAX_LOANS = 3

    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, value):
        self.__member_id = member_id_validator(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = name_validator(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = email_validator(value)

    def to_dict(self):
        return {"member_id": self.member_id, "name": self.name, "email": self.email}

    def __str__(self):
        return f"[{self.member_id}] {self.name} <{self.email}>"
