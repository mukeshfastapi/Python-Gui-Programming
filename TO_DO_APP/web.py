import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new = st.session_state["new_todo"] + '\n'
    todos.append(new)
    functions.write_todos(todos)

st.title ('My ToDo App')
st.subheader("This is my ToDo App")
st.write("This App will increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo:",
              on_change=add_todo, key='new_todo')
