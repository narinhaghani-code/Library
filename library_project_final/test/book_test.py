from model.book import Book

# OK
book = Book(1, "1234567890", "Python", "John Smith", 2020, 3)
print(book)

# ERROR
try:
    book = Book(-1, "1234567890", "Python", "Narin Haghani", 2020, 3)
except ValueError as error:
    print("Error:", error)

try:
    book = Book(2, "123", "Python", "John Smith", 2020, 3)
except ValueError as error:
    print("Error:", error)

try:
    book = Book(3, "1234567890", "Python", "Narin Haghani", 99, 3)
except ValueError as error:
    print("Error:", error)

try:
    book = Book(4, "1234567890", "Python", "John Smith", 2020, 0)
except ValueError as error:
    print("Error:", error)
