import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in To-Do")
input_text = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label, input_text, add_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break
window.read()
window.close()





