import streamlit as st

with st.form("contact_us"):
    st.title("Contact Us")

    email_address = st.text_input("Your email address")
    message = st.text_area("Your message")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("From ", email_address, "message", message)
