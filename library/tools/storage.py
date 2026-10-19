import json
import os
from datetime import date
from tools.exceptions import LibraryError
from models.book import Book
from models.member import Member
from models.borrow import Borrow



class JsonStorage:
    def __init__(self, path="data/library.json"):
        self.path = path

    def save(self, library):
        folder = os.path.dirname(self.path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(library.to_dict(), file, indent=2)

    def load(self):
        library = Library()
        if not os.path.exists(self.path):
            return library
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                data = json.load(file)
            for item in data["books"]:
                book = Book(item["isbn"], item["title"], item["author"], item["year"], item["copies_total"])
                book.copies_available = item["copies_available"]
                library.books.append(book)
            for item in data["members"]:
                library.members.append(Member(item["member_id"], item["name"], item["email"]))
            for item in data["borrows"]:
                return_date = None
                if item["return_date"] is not None:
                    return_date = date.fromisoformat(item["return_date"])
                borrow = Borrow(item["borrow_id"], item["isbn"], item["member_id"],
                                date.fromisoformat(item["borrow_date"]),
                                date.fromisoformat(item["due_date"]), return_date)
                library.borrows.append(borrow)
            library.next_borrow_id = data["next_borrow_id"]
        except (json.JSONDecodeError, KeyError, ValueError):
            raise LibraryError("Data file is damaged")
        return library
