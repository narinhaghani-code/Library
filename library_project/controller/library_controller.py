from tools.exceptions import LibraryError
from models.book import Book
from models.member import Member


class LibraryController:
    def __init__(self, library, storage, view):
        self.library = library
        self.storage = storage
        self.view = view

    def run(self):
        while True:
            choice = self.view.show_menu()
            try:
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.add_member()
                elif choice == "3":
                    self.list_books()
                elif choice == "4":
                    self.list_members()
                elif choice == "5":
                    self.search_books()
                elif choice == "6":
                    self.borrow_book()
                elif choice == "7":
                    self.return_book()
                elif choice == "8":
                    self.show_active_borrows()
                elif choice == "9":
                    self.show_overdue_borrows()
                elif choice == "0":
                    self.storage.save(self.library)
                    self.view.show_message("Data saved")
                    break
                else:
                    self.view.show_error("Unknown option")
                    continue
                self.storage.save(self.library)
            except (ValueError, LibraryError) as error:
                self.view.show_error(str(error))

    def ask_int(self, prompt):
        text = self.view.ask(prompt)
        if not text.isdigit():
            raise ValueError("Please enter a number")
        return int(text)

    def add_book(self):
        isbn = self.view.ask("ISBN")
        title = self.view.ask("Title")
        author = self.view.ask("Author")
        year = self.ask_int("Year")
        copies = self.ask_int("Number of copies")
        self.library.add_book(Book(isbn, title, author, year, copies))
        self.view.show_message("Book added")

    def add_member(self):
        member_id = self.view.ask("Member ID")
        name = self.view.ask("Name")
        email = self.view.ask("Email")
        self.library.add_member(Member(member_id, name, email))
        self.view.show_message("Member added")

    def list_books(self):
        self.view.show_list("Books", self.library.books)

    def list_members(self):
        self.view.show_list("Members", self.library.members)

    def search_books(self):
        keyword = self.view.ask("Search (title, author or ISBN)")
        self.view.show_list("Results", self.library.search_books(keyword))

    def borrow_book(self):
        isbn = self.view.ask("ISBN")
        member_id = self.view.ask("Member ID")
        borrow = self.library.borrow_book(isbn, member_id)
        self.view.show_message(f"Borrowed. Due date: {borrow.due_date}")

    def return_book(self):
        fine = self.library.return_book(self.ask_int("Borrow record number"))
        if fine > 0:
            self.view.show_message(f"Returned late. Fine: {fine:.2f}")
        else:
            self.view.show_message("Returned on time.")

    def show_active_borrows(self):
        self.view.show_list("Active borrows", self.library.active_borrows())

    def show_overdue_borrows(self):
        self.view.show_list("Overdue borrows", self.library.overdue_borrows())
