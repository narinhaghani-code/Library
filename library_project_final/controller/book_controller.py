from model.book import Book
from tools.file_manager import *
from tools.validation import id_validator


class BookController:
    def __init__(self, storage, path):
        self.storage = storage
        self.path = path
        self.load()

    def load(self):
        try:
            for item in load_items(self.path):
                book = Book(item["book_id"], item["isbn"], item["title"], item["author"], item["year"], item["copies"])
                book.available = item["available"]
                self.storage.add_book(book)
        except (KeyError, TypeError, ValueError):
            raise ValueError("Data file is damaged")

    def save(self):
        items = []
        for book in self.storage.books:
            items.append(book.to_dict())
        save_items(self.path, items)

    def add_book(self, book_id, isbn, title, author, year, copies):
        book = Book(book_id, isbn, title, author, year, copies)
        self.storage.add_book(book)
        self.save()
        return book

    def get_book(self, book_id):
        return self.storage.get_book(id_validator(book_id, "Book ID"))

    def search_books(self, keyword):
        return self.storage.search(keyword)

    def all_books(self):
        return self.storage.books
