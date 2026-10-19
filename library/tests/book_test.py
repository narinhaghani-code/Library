import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.book import Book

# OK
book = Book("1234567890", "Python", "John Smith", 2020, 3)
print(book.__dict__)

# ERROR
try:
    book = Book("123", "English", "Ali Aliyi", 2020, 3)
    print(book.__dict__)
except ValueError as error:
    print("Error:", error)

try:
    book = Book("1234567890", "Math", "Naz Rezayi", 99, 3)
    print(book.__dict__)
except ValueError as error:
    print("Error:", error)
