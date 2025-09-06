import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    new = st.session_state["new_todo"] + '\n'
    todos.append(new)
    functions.write_todos(todos)

st.title ('My ToDo App')
st.subheader("This is my ToDo App")
st.write("<h2>This App will increase your <b>productivity</b></h2>",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new todo:",
              on_change=add_todo, key='new_todo')

for index,todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



