from datetime import date, timedelta
from model.borrow import Borrow
from model.member import Member
from tools.file_manager import *
from tools.validation import id_validator


class BorrowController:
    def __init__(self, path, book_controller, member_controller):
        self.path = path
        self.book_controller = book_controller
        self.member_controller = member_controller
        self.borrows = []
        self.load()

    def load(self):
        try:
            for item in load_items(self.path):
                return_date = None
                if item["return_date"] is not None:
                    return_date = date.fromisoformat(item["return_date"])
                self.borrows.append(Borrow(item["borrow_id"], item["book_id"], item["member_id"], date.fromisoformat(item["borrow_date"]), date.fromisoformat(item["due_date"]), return_date))
        except (KeyError, TypeError, ValueError):
            raise ValueError("Data file is damaged")

    def save(self):
        items = []
        for borrow in self.borrows:
            items.append(borrow.to_dict())
        save_items(self.path, items)

    def next_id(self):
        biggest = 0
        for borrow in self.borrows:
            if borrow.borrow_id > biggest:
                biggest = borrow.borrow_id
        return biggest + 1

    def active_borrows(self, member_id=None):
        result = []
        for borrow in self.borrows:
            if not borrow.is_returned() and (member_id is None or borrow.member_id == member_id):
                result.append(borrow)
        return result

    def overdue_borrows(self, today=None):
        result = []
        for borrow in self.active_borrows():
            if borrow.is_overdue(today):
                result.append(borrow)
        return result

    def borrow_book(self, book_id, member_id, today=None):
        if today is None:
            today = date.today()
        book = self.book_controller.get_book(book_id)
        member = self.member_controller.get_member(member_id)
        active = self.active_borrows(member.member_id)

        if len(active) >= Member.MAX_LOANS:
            raise ValueError(f"{member.name} already has {Member.MAX_LOANS} books")
        for borrow in active:
            if borrow.is_overdue(today):
                raise ValueError(f"{member.name} has an overdue book")
            if borrow.book_id == book.book_id:
                raise ValueError(f"{member.name} already borrowed this book")

        book.take_copy()
        due_date = today + timedelta(days=Borrow.LOAN_DAYS)
        borrow = Borrow(self.next_id(), book.book_id, member.member_id, today, due_date)
        self.borrows.append(borrow)
        self.book_controller.save()
        self.save()
        return borrow

    def return_book(self, borrow_id, today=None):
        if today is None:
            today = date.today()
        borrow_id = id_validator(borrow_id, "Borrow ID")
        for borrow in self.borrows:
            if borrow.borrow_id == borrow_id:
                if borrow.is_returned():
                    raise ValueError("This book was already returned")
                borrow.return_date = today
                self.book_controller.get_book(borrow.book_id).give_back_copy()
                self.book_controller.save()
                self.save()
                return borrow.fine()
        raise ValueError(f"No borrow with ID {borrow_id}")
