import streamlit as st

from send_email import send_email

st.header('Contact Me')

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    button = st.form_submit_button()
    email_content = f"""\
Subject: Email from {user_email}
    

From: {user_email}
{user_message}
"""
    if button:
        send_email(email_content)
        st.info('Message Sent!')
