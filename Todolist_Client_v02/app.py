import streamlit as st
import requests

BASE_URL="http://localhost:8000"


def login():
    st.title("Login")
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password",type="password")
        submit = st.form_submit_button("Login")
        if submit:

            response = requests.post(BASE_URL+" /users/authenticate",json={
                "name":username,
                "password":password
            })
            if response.status_code==200:
                user_data= response.json()


          