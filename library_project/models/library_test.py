import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import date
from models.book import Book
from models.member import Member
from models.library import Library
from tools.exceptions import LibraryError
from tools.storage import JsonStorage

library = Library()
library.add_book(Book("1234567890", "Python Basics", "John Smith", 2020, 2))
library.add_book(Book("1111111111", "Java Basics", "Mary Jones", 2019, 1))
library.add_member(Member("M0001", "Alice Brown", "alice@example.com"))
library.add_member(Member("M0002", "Bob White", "bob@example.com"))

# OK - borrow and return on time
borrow = library.borrow_book("1234567890", "M0001")
print(borrow)
print(library.get_book("1234567890"))
print("Fine:", library.return_book(borrow.borrow_id))

# OK - return 5 days late
borrow = library.borrow_book("1234567890", "M0001", today=date(2024, 1, 1))
print("Fine:", library.return_book(borrow.borrow_id, today=date(2024, 1, 20)))

# ERROR - same ISBN twice
try:
    library.add_book(Book("1234567890", "Another Title", "John Smith", 2021, 1))
except LibraryError as error:
    print("Error:", error)

# ERROR - borrow the same book twice
library.borrow_book("1234567890", "M0001")
try:
    library.borrow_book("1234567890", "M0001")
except LibraryError as error:
    print("Error:", error)

# ERROR - unknown book / unknown member
try:
    library.borrow_book("9999999999", "M0001")
except LibraryError as error:
    print("Error:", error)
try:
    library.borrow_book("1234567890", "M9999")
except LibraryError as error:
    print("Error:", error)

# ERROR - remove a book that is borrowed
try:
    library.remove_book("1234567890")
except LibraryError as error:
    print("Error:", error)

# ERROR - member with an overdue book cannot borrow
library.borrow_book("1111111111", "M0002", today=date(2020, 1, 1))
try:
    library.borrow_book("1234567890", "M0002")
except LibraryError as error:
    print("Error:", error)
print("Overdue:", [str(item) for item in library.overdue_borrows()])

# ERROR - more than 3 books at the same time
library.add_member(Member("M0003", "Carol Green", "carol@example.com"))
for number in range(1, 5):
    library.add_book(Book("200000000" + str(number), "Book " + str(number), "John Smith", 2020, 1))
for number in range(1, 4):
    library.borrow_book("200000000" + str(number), "M0003")
try:
    library.borrow_book("2000000004", "M0003")
except LibraryError as error:
    print("Error:", error)

# OK - save to a file and load it again
storage = JsonStorage("test_data.json")
storage.save(library)
loaded = storage.load()
os.remove("test_data.json")
print("Books:", len(loaded.books), "| Members:", len(loaded.members),
      "| Active borrows:", len(loaded.active_borrows()))
