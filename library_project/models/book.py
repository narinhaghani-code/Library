from tools.validation import *
from tools.exceptions import LibraryError


class Book:
    def __init__(self, isbn, title, author, year, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.copies_total = copies
        self.copies_available = copies

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = isbn_validator(value)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = title_validator(value)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = author_validator(value)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = year_validator(value)

    @property
    def copies_total(self):
        return self.__copies_total

    @copies_total.setter
    def copies_total(self, value):
        self.__copies_total = count_validator(value, 1)

    @property
    def copies_available(self):
        return self.__copies_available

    @copies_available.setter
    def copies_available(self, value):
        value = count_validator(value)
        if value > self.copies_total:
            raise ValueError("Available copies cannot exceed total copies")
        self.__copies_available = value

    def is_available(self):
        return self.copies_available > 0

    def take_copy(self):
        if not self.is_available():
            raise LibraryError(f"No copies of '{self.title}' are available")
        self.copies_available -= 1

    def give_back_copy(self):
        self.copies_available += 1

    def matches(self, keyword):
        keyword = keyword.lower()
        if keyword in self.title.lower() or keyword in self.author.lower() or keyword == self.isbn:
            return True
        return False

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "copies_total": self.copies_total,
            "copies_available": self.copies_available,
        }

    def __str__(self):
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) - {self.copies_available}/{self.copies_total} available"
