import streamlit as st
import re


def username_validation(user):
    return bool(re.search(r"[a-zA-Z]", user)) and bool(re.search(r"\d", user))


st.title("Register")

username = st.text_input("Username")
if username:
    if len(username) <8:
        st.error("Username must be 8 or more characters")
    if not username_validation(username):
        st.error("Username must contain letters and numbers")




password = st.text_input("Password", type="password")
if password:
    if len(password) <8:
        st.error ("Password must be 8 or more characters")



confirm_pass = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    if password == confirm_pass:
        st.success("Registration Successful!")
    else:
        st.error("Passwords are not equal!")

