import os
from datetime import date
from model.storage import Storage
from controller.book_controller import BookController
from controller.member_controller import MemberController
from controller.borrow_controller import BorrowController

files = ["test_books.json", "test_members.json", "test_borrows.json"]
for name in files:
    if os.path.exists(name):
        os.remove(name)

books = BookController(Storage(1, "Main Hall", 10), "test_books.json")
members = MemberController("test_members.json")
borrows = BorrowController("test_borrows.json", books, members)

books.add_book("1", "1234567890", "Python Basics", "John Smith", "2020", "2")
books.add_book("2", "1111111111", "Java", "Mary Jones", "2019", "1")
members.add_member("1", "Alice Brown", "alice@example.com")
members.add_member("2", "Bob Rad", "bob@example.com")

# OK - borrow and return on time
borrow = borrows.borrow_book("1", "1")
print(borrow)
print("Fine:", borrows.return_book(borrow.borrow_id))

# OK - return 5 days late
borrow = borrows.borrow_book("1", "1", today=date(2024, 1, 1))
print("Fine:", borrows.return_book(borrow.borrow_id, today=date(2024, 1, 20)))

# ERROR - same book ID twice / year not a number / same member twice
for action in [lambda: books.add_book("1", "2222222222", "Other Book", "John Smith", "2021", "1"),
               lambda: books.add_book("9", "2222222222", "Other Book", "John Smith", "abc", "1"),
               lambda: members.add_member("1", "Alice Brown", "alice@example.com")]:
    try:
        action()
    except ValueError as error:
        print("Error:", error)

# ERROR - same book twice, unknown book, unknown member
borrows.borrow_book("1", "1")
for action in [lambda: borrows.borrow_book("1", "1"),
               lambda: borrows.borrow_book("99", "1"),
               lambda: borrows.borrow_book("1", "99")]:
    try:
        action()
    except ValueError as error:
        print("Error:", error)

# ERROR - member with an overdue book cannot borrow
borrows.borrow_book("2", "2", today=date(2020, 1, 1))
try:
    borrows.borrow_book("1", "2")
except ValueError as error:
    print("Error:", error)
print("Overdue:", [str(item) for item in borrows.overdue_borrows()])

# ERROR - more than 3 books
members.add_member("3", "Narin Haghani", "narin@example.com")
for number in range(3, 7):
    books.add_book(str(number), f"300000000{number}", f"Book {number}", "John Smith", "2020", "1")
for number in range(3, 6):
    borrows.borrow_book(str(number), "3")
try:
    borrows.borrow_book("6", "3")
except ValueError as error:
    print("Error:", error)

# ERROR - return twice / unknown borrow
for value in ["1", "999"]:
    try:
        borrows.return_book(value)
    except ValueError as error:
        print("Error:", error)

# OK - load again from the files
books2 = BookController(Storage(1, "Main Hall", 10), "test_books.json")
members2 = MemberController("test_members.json")
borrows2 = BorrowController("test_borrows.json", books2, members2)
print("Books:", len(books2.all_books()), "| Members:", len(members2.members),
      "| Active borrows:", len(borrows2.active_borrows()))

for name in files:
    os.remove(name)
