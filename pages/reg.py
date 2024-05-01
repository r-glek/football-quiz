import pandas as pd
import streamlit as st
import re


def validation_alphanum(user):
    return bool(re.search(r'[a-zA-Z]', user)) and bool(re.search(r'\d', user))


def validation_symbols(pass_local):
    return bool(re.search(r'[^a-zA-Z0-9]', pass_local))


def validate_registration(user, pass_arg, confirm_password):
    df = pd.read_csv("users.csv")
    errors = []

    # Checks username
    if len(user) < 8:
        errors.append("Username must be 8 or more chars")
    elif not validation_alphanum(user):
        errors.append("Username must contains letters and numbers")
    elif (df['username'] == user).any():
        errors.append("Username already exists.")

    # Checks password
    if len(pass_arg) < 8:
        errors.append("Password must be 8 or more chars")
    elif not validation_alphanum(pass_arg):
        errors.append("Password must contains letters and numbers")
    elif not validation_symbols(pass_arg):
        errors.append("Password must contain symbol(s)")

    # Checks confirmed password
    if pass_arg != confirm_password:
        errors.append("Passwords do not match")

    return errors


def add_user(user, pass_arg, filename="users.csv"):

    # Convert new user to dict
    new_user = {"username": [user], "password": [pass_arg]}
    # Convert dict to dataframe
    new_user_df = pd.DataFrame(new_user)

    # reading users from file as dataframe
    df = pd.read_csv(filename)
    # Combining new user df with file df
    df = pd.concat([df, new_user_df])
    # Overwriting users in file
    df.to_csv(filename, index=False)


# Widgets
st.title("Register")

register_info = '''
Username requirements:
- 8 or more characters
- must contain letters and numbers

Password requirements:
- 8 or more characters
- must contain letters and numbers
- must contain a symbol
'''

st.info(register_info)

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_pass = st.text_input("Confirm Password", type="password")

if st.button("Register"):
    validation_errors = validate_registration(username, password, confirm_pass)
    if not validation_errors:
        add_user(username, password)
        st.success("Registration successful.")
    else:
        for item in validation_errors:
            st.error(item)

# pip install captcha streamlit


# import library
import streamlit as st
from captcha.image import ImageCaptcha
import random, string

# define the costant
length_captcha = 4
width = 200
height = 150


# define the function for the captcha control
def captcha_control():
    # control if the captcha is correct
    if 'controllo' not in st.session_state or st.session_state['controllo'] == False:
        st.title("Captcha Control on Streamlit🤗")

        # define the session state for control if the captcha is correct
        st.session_state['controllo'] = False
        col1, col2 = st.columns(2)

        # define the session state for the captcha text because it doesn't change during refreshes
        if 'Captcha' not in st.session_state:
            st.session_state['Captcha'] = ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=length_captcha))
        print("the captcha is: ", st.session_state['Captcha'])

        # setup the captcha widget
        image = ImageCaptcha(width=width, height=height)
        data = image.generate(st.session_state['Captcha'])
        col1.image(data)
        capta2_text = col2.text_area('Enter captcha text', height=30)

        if st.button("Verify the code"):
            print(capta2_text, st.session_state['Captcha'])
            capta2_text = capta2_text.replace(" ", "")
            # if the captcha is correct, the controllo session state is set to True
            if st.session_state['Captcha'].lower() == capta2_text.lower().strip():
                del st.session_state['Captcha']
                col1.empty()
                col2.empty()
                st.session_state['controllo'] = True
                st.experimental_rerun()
            else:
                # if the captcha is wrong, the controllo session state is set to False and the captcha is regenerated
                st.error("🚨 Il codice captcha è errato, riprova")
                del st.session_state['Captcha']
                del st.session_state['controllo']
                st.experimental_rerun()
        else:
            # wait for the button click
            st.stop()


def your_main():
    st.title("Congratulation you are not a robot🤖")
    st.write("You can use this app without problems")

    # ADD HERE YOUR CODE

    if st.button("Go back to the main app"):
        del st.session_state['controllo']
        st.experimental_rerun()


# WORK LIKE MULTIPAGE APP
if 'controllo' not in st.session_state or st.session_state['controllo'] == False:
    captcha_control()
else:
    your_main()