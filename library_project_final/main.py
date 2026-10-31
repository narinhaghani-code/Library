import os
import streamlit as st
from model.storage import Storage
from controller.book_controller import BookController
from controller.member_controller import MemberController
from controller.borrow_controller import BorrowController
from view.menu import show_menu

folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

try:
    storage = Storage(1, "Main Hall", 100)
    book_controller = BookController(storage, os.path.join(folder, "books.json"))
    member_controller = MemberController(os.path.join(folder, "members.json"))
    borrow_controller = BorrowController(os.path.join(folder, "borrows.json"), book_controller, member_controller)
except ValueError as error:
    st.error(str(error))
    st.stop()

show_menu(book_controller, member_controller, borrow_controller)
