from model.book import Book
from model.storage import Storage

# OK
storage = Storage(1, "Main Hall", 2)
storage.add_book(Book(1, "1234567890", "Python", "John Smith", 2020, 3))
storage.add_book(Book(2, "1111111111", "Java", "Mary Jones", 2019, 1))
print(storage)
print("Search:", [str(book) for book in storage.search("java")])

# ERROR
try:
    storage.add_book(Book(3, "2222222222", "Math", "Naz Rezayi", 2018, 1))
except ValueError as error:
    print("Error:", error)

try:
    storage = Storage(0, "Main Hall", 2)
except ValueError as error:
    print("Error:", error)

try:
    storage = Storage(1, "Main Hall", "many")
except ValueError as error:
    print("Error:", error)
