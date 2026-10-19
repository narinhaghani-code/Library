class ConsoleView:
    MENU = """
===== Library Menu =====
1. Add book
2. Add member
3. List books
4. List members
5. Search books
6. Borrow a book
7. Return a book
8. Show active borrows
9. Show overdue borrows
0. Exit"""

    def show_menu(self):
        print(self.MENU)
        return input("Choose: ").strip()

    def ask(self, prompt):
        return input(prompt + ": ").strip()

    def show_message(self, text):
        print(text)

    def show_error(self, text):
        print(f"Error: {text}")

    def show_list(self, title, items):
        print(f"\n--- {title} ---")
        if len(items) == 0:
            print("(nothing to show)")
        for item in items:
            print(item)
