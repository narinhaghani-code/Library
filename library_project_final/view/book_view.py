import streamlit as st


def show_book_page(controller):
    st.header("Books")
    with st.form("book_form"):
        book_id = st.text_input("Book ID")
        isbn = st.text_input("ISBN")
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.text_input("Year")
        copies = st.text_input("Copies")
        entered = st.form_submit_button("Enter ✓")

    if entered:
        try:
            controller.add_book(book_id.strip(), isbn.strip(), title.strip(), author.strip(), year.strip(), copies.strip())
            st.success("Book added")
        except ValueError as error:
            st.error(str(error))

    st.subheader("All books")
    books = controller.all_books()
    if len(books) == 0:
        st.text("No books yet")
    for book in books:
        st.text(str(book))
