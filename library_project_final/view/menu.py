import streamlit as st
from view.book_view import show_book_page
from view.member_view import show_member_page
from view.borrow_view import show_borrow_page


def show_menu(book_controller, member_controller, borrow_controller):
    st.title("Library Management")
    st.write("Welcome")
    page = st.sidebar.selectbox("Menu", ["Books", "Members", "Borrow"])
    if page == "Books":
        show_book_page(book_controller)
    elif page == "Members":
        show_member_page(member_controller)
    else:
        show_borrow_page(borrow_controller)
