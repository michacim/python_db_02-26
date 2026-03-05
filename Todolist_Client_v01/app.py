import streamlit as st
import requests

BASE_URL="http://127.0.0.1:8000"

try:

    response = requests.get(BASE_URL,timeout=5)
    if response.status_code== 200:
        print("Server erreichbar")
    else:
        print(f"Server Statuscode: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Server nicht erreichbar: {e}")

st.title("Neues Todo")
user_id = st.number_input("User-Id",min_value=1,step=1, format="%d")
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
    if st.button("Todoerstellen"):
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