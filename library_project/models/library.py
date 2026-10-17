from datetime import date, timedelta
from tools.exceptions import LibraryError
from models.book import Book
from models.member import Member
from models.borrow import Borrow


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrows = []
        self.next_borrow_id = 1

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid Book")
        for item in self.books:
            if item.isbn == book.isbn:
                raise LibraryError(f"A book with ISBN {book.isbn} already exists")
        self.books.append(book)

    def get_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        raise LibraryError(f"No book with ISBN {isbn}")

    def remove_book(self, isbn):
        book = self.get_book(isbn)
        for borrow in self.borrows:
            if borrow.isbn == isbn and not borrow.is_returned():
                raise LibraryError("Cannot remove a book that is currently borrowed")
        self.books.remove(book)

    def search_books(self, keyword):
        result = []
        for book in self.books:
            if book.matches(keyword):
                result.append(book)
        return result

    def add_member(self, member):
        if not isinstance(member, Member):
            raise ValueError("Invalid Member")
        for item in self.members:
            if item.member_id == member.member_id:
                raise LibraryError(f"Member {member.member_id} already exists")
        self.members.append(member)

    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        raise LibraryError(f"No member with ID {member_id}")

    def remove_member(self, member_id):
        member = self.get_member(member_id)
        if len(self.active_borrows_of(member_id)) > 0:
            raise LibraryError("Cannot remove a member who still has borrowed books")
        self.members.remove(member)

    def active_borrows_of(self, member_id):
        result = []
        for borrow in self.borrows:
            if borrow.member_id == member_id and not borrow.is_returned():
                result.append(borrow)
        return result

    def active_borrows(self):
        result = []
        for borrow in self.borrows:
            if not borrow.is_returned():
                result.append(borrow)
        return result

    def overdue_borrows(self, today=None):
        result = []
        for borrow in self.active_borrows():
            if borrow.is_overdue(today):
                result.append(borrow)
        return result

    def borrow_book(self, isbn, member_id, today=None):
        if today is None:
            today = date.today()
        book = self.get_book(isbn)
        member = self.get_member(member_id)
        active = self.active_borrows_of(member_id)

        if len(active) >= Member.MAX_LOANS:
            raise LibraryError(f"{member.name} already has {Member.MAX_LOANS} books")
        for borrow in active:
            if borrow.is_overdue(today):
                raise LibraryError(f"{member.name} has overdue books and must return them")
        for borrow in active:
            if borrow.isbn == isbn:
                raise LibraryError(f"{member.name} already borrowed this book")

        book.take_copy()
        due_date = today + timedelta(days=Borrow.LOAN_DAYS)
        borrow = Borrow(self.next_borrow_id, isbn, member_id, today, due_date)
        self.next_borrow_id += 1
        self.borrows.append(borrow)
        return borrow

    def return_book(self, borrow_id, today=None):
        borrow = None
        for item in self.borrows:
            if item.borrow_id == borrow_id:
                borrow = item
        if borrow is None:
            raise LibraryError(f"No borrow record {borrow_id}")
        if borrow.is_returned():
            raise LibraryError("This book was already returned")
        borrow.mark_returned(today)
        self.get_book(borrow.isbn).give_back_copy()
        return borrow.fine()

    def to_dict(self):
        books = []
        for book in self.books:
            books.append(book.to_dict())
        members = []
        for member in self.members:
            members.append(member.to_dict())
        borrows = []
        for borrow in self.borrows:
            borrows.append(borrow.to_dict())
        return {
            "books": books,
            "members": members,
            "borrows": borrows,
            "next_borrow_id": self.next_borrow_id,
        }
