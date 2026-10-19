from datetime import date
from tools.validation import *


class Borrow:
    LOAN_DAYS = 14
    FINE_PER_DAY = 0.5

    def __init__(self, borrow_id, isbn, member_id, borrow_date, due_date, return_date=None):
        self.borrow_id = borrow_id
        self.isbn = isbn
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date

    @property
    def borrow_id(self):
        return self.__borrow_id

    @borrow_id.setter
    def borrow_id(self, value):
        self.__borrow_id = borrow_id_validator(value)

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = isbn_validator(value)

    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, value):
        self.__member_id = member_id_validator(value)

    @property
    def borrow_date(self):
        return self.__borrow_date

    @borrow_date.setter
    def borrow_date(self, value):
        self.__borrow_date = date_validator(value)

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        value = date_validator(value)
        if value < self.borrow_date:
            raise ValueError("Due date cannot be before borrow date")
        self.__due_date = value

    @property
    def return_date(self):
        return self.__return_date

    @return_date.setter
    def return_date(self, value):
        if value is not None:
            value = date_validator(value)
            if value < self.borrow_date:
                raise ValueError("Return date cannot be before borrow date")
        self.__return_date = value

    def is_returned(self):
        return self.return_date is not None

    def is_overdue(self, today=None):
        if today is None:
            today = date.today()
        if self.is_returned():
            end = self.return_date
        else:
            end = today
        return end > self.due_date

    def fine(self, today=None):
        if today is None:
            today = date.today()
        if self.is_returned():
            end = self.return_date
        else:
            end = today
        late_days = (end - self.due_date).days
        if late_days < 0:
            late_days = 0
        return late_days * Borrow.FINE_PER_DAY

    def mark_returned(self, today=None):
        if today is None:
            today = date.today()
        self.return_date = today

    def to_dict(self):
        if self.is_returned():
            return_date = self.return_date.isoformat()
        else:
            return_date = None
        return {
            "borrow_id": self.borrow_id,
            "isbn": self.isbn,
            "member_id": self.member_id,
            "borrow_date": self.borrow_date.isoformat(),
            "due_date": self.due_date.isoformat(),
            "return_date": return_date,
        }

    def __str__(self):
        if self.is_returned():
            status = f"returned {self.return_date}"
        else:
            status = f"due {self.due_date}"
        return f"#{self.borrow_id}: book {self.isbn} -> member {self.member_id} ({status})"
