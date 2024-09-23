import streamlit as st
from send_email import send_email


st.header("Contact Us")
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submitted = st.form_submit_button("Submit")
    if submitted:
        send_email(message, user_email)
        st.info("Email sent successfully")
