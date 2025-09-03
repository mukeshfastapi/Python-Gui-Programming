import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in To-Do")
input_text = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True, size=[45,20])
edit_button = sg.Button('Edit')


window = sg.Window("My To-Do App", layout=[[label, input_text, add_button],
                                           [list_box, edit_button]],
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
            window['todos'].update (values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window['todos'].update(values= todos)
        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case sg.WINDOW_CLOSED:
            break
window.read()
window.close()





