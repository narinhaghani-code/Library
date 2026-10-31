from tools.validation import *


class Storage:
    def __init__(self, storage_id, location, capacity):
        self.storage_id = storage_id
        self.location = location
        self.capacity = capacity
        self.__books = []

    @property
    def storage_id(self):
        return self.__storage_id

    @storage_id.setter
    def storage_id(self, value):
        self.__storage_id = id_validator(value, "Storage ID")

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = location_validator(value)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = count_validator(value, "Capacity", 1)

    @property
    def books(self):
        return list(self.__books)

    def add_book(self, book):
        if len(self.__books) >= self.capacity:
            raise ValueError("Storage is full")
        for item in self.__books:
            if item.book_id == book.book_id:
                raise ValueError(f"A book with ID {book.book_id} already exists")
        self.__books.append(book)

    def get_book(self, book_id):
        for item in self.__books:
            if item.book_id == book_id:
                return item
        raise ValueError(f"No book with ID {book_id}")

    def search(self, keyword):
        keyword = keyword.lower()
        result = []
        for item in self.__books:
            if keyword in item.title.lower() or keyword in item.author.lower() or keyword == item.isbn or keyword == str(item.book_id):
                result.append(item)
        return result

    def __str__(self):
        return f"Storage {self.storage_id} at {self.location} ({len(self.__books)}/{self.capacity} books)"
