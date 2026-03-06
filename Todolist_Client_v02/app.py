import streamlit as st
import requests

BASE_URL="http://localhost:8000"


def login():
    st.title("Login")
    with st.form(key="login_form"): # key: id für Formular
        username = st.text_input("Username")
        password = st.text_input("Password",type="password")
        submit = st.form_submit_button("Login")
        if submit:

            response = requests.post(BASE_URL+"/users/authenticate",json={
                "username":username,
                "password":password
            })
            if response.status_code==200:
                user_data= response.json()
                st.session_state["user"] = user_data#
                st.success(f"Welcome, {user_data['username']}")  # Message
                st.session_state["logged_in"]=True
                st.rerun()#läd die Seite neu
            else:
                st.error("Name oder Passwort falsch! "+str(response.status_code))

def welcome():
    #user = st.session_state.get("username")# Userdaten aus der Session holen
    user = st.session_state.get("user")# Userdaten aus der Session holen
    user_id = user['id']
    st.title(f"Wilkommen,  {user['username']}") 
    # ------------------------------------------------------------
    st.title("Neues Todo")
    #user_id = st.number_input("User-Id",min_value=1,step=1, format="%d")
    task = st.text_input("Task")
    description = st.text_input("Description")
    deadline = st.date_input("Deadline",format="DD.MM.YYYY")
    state =st.selectbox("State",["OPEN","IN_PROGRESS","DONE"])
    json_param ={
        "task":task,
        "description":description,
        "deadline":deadline.isoformat(),
        "state":state
    }
    try:
        if st.button("Todo erstellen"):
            response = requests.post(f"{BASE_URL}/todos/",json=json_param, params={"user_id":user_id} )
            if response.status_code ==200:
                st.success("Todo gespeichert!")
                st.json(response.json())
            else:
                st.error(response.status_code)
        st.write("Todos")
        response = requests.get(f"{BASE_URL}/users/{user_id}/todos")# http://localhost:8000/users/2/todos
        response.raise_for_status() # prüft auf http-code 200
        todos = response.json()
        if todos:
            st.table(todos)
        else:
            st.info("keine Todos")
    except requests.exceptions.RequestException as e:
        print(f"Server nicht erreichbar: {e}")

def logout():
    st.session_state['logged_in'] = False
    st.session_state.pop("user",None) #user aus Session entfernen
    st.success("Erfolgreich abgelmeldet!")
    st.rerun()


if st.session_state.get('logged_in'):
    if st.button("Logout"):
        logout()
if "logged_in" not in st.session_state:
    st.session_state['logged_in']=False
if st.session_state['logged_in']:
    welcome()
else:
    login()