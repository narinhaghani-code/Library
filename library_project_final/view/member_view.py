import streamlit as st


def show_member_page(controller):
    st.header("Members")
    with st.form("member_form"):
        member_id = st.text_input("Member ID")
        name = st.text_input("Name")
        email = st.text_input("Email")
        entered = st.form_submit_button("Enter ✓")

    if entered:
        try:
            controller.add_member(member_id.strip(), name.strip(), email.strip())
            st.success("Member added")
        except ValueError as error:
            st.error(str(error))

    st.subheader("All members")
    if len(controller.members) == 0:
        st.text("No members yet")
    for member in controller.members:
        st.text(str(member))
