from tools.validation import *


class Book:
    def __init__(self, book_id, isbn, title, author, year, copies):
        self.book_id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.available = copies

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, value):
        self.__book_id = id_validator(value, "Book ID")

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
        self.__author = name_validator(value)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = year_validator(value)

    @property
    def copies(self):
        return self.__copies

    @copies.setter
    def copies(self, value):
        self.__copies = count_validator(value, "Copies", 1)

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        value = count_validator(value, "Available copies", 0)
        if value > self.copies:
            raise ValueError("Available copies cannot be more than copies")
        self.__available = value

    def take_copy(self):
        if self.available == 0:
            raise ValueError("No copy of this book is available")
        self.available = self.available - 1

    def give_back_copy(self):
        self.available = self.available + 1

    def to_dict(self):
        return {"book_id": self.book_id, "isbn": self.isbn, "title": self.title, "author": self.author, "year": self.year, "copies": self.copies, "available": self.available}

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} ({self.year}) - {self.available}/{self.copies} available"
