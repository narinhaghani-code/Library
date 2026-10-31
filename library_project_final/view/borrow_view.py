import streamlit as st


def show_borrow_page(controller):
    st.header("Borrow")
    col1, col2 = st.columns(2)

    with col1:
        with st.form("borrow_form"):
            member_id = st.text_input("Member ID")
            book_id = st.text_input("Book ID")
            entered = st.form_submit_button("Enter ✓")

    with col2:
        with st.form("return_form"):
            borrow_id = st.text_input("Borrow ID")
            returned = st.form_submit_button("Return ✓")

    if entered:
        try:
            borrow = controller.borrow_book(book_id.strip(), member_id.strip())
            st.success(f"Borrowed. Due date: {borrow.due_date}")
        except ValueError as error:
            st.error(str(error))

    if returned:
        try:
            fine = controller.return_book(borrow_id.strip())
            if fine > 0:
                st.success(f"Returned late. Fine: {fine:.2f}")
            else:
                st.success("Returned on time.")
        except ValueError as error:
            st.error(str(error))

    st.subheader("All borrows")
    if len(controller.borrows) == 0:
        st.text("No borrows yet")
    for borrow in controller.borrows:
        st.text(str(borrow))
