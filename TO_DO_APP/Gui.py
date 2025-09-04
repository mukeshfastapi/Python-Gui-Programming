import functions
import FreeSimpleGUI as sg
import time

sg.theme('DarkPurple4')
clock = sg.Text('', key='clock')
label = sg.Text("Type in To-Do")
input_text = sg.InputText(tooltip="Enter a to-do", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True, size=[45,20])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window("My To-Do App", layout=[[clock],
                                           [label],
                                           [input_text, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update (values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos ()
                index = todos.index (todo_to_edit)
                todos[index] = new_todo
                functions.write_todos (todos)
                window['todos'].update (values=todos)
            except IndexError:
                sg.popup("Please select an item,",font=("Helvetica",15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos ()
                todos.remove (todo_to_complete)
                functions.write_todos (todos)
                window['todos'].update (values=todos)
                window['todo'].update (value="")
            except IndexError:
                sg.popup("Please select an item,",font=("Helvetica",15))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value = values['todos'][0])

        case sg.WINDOW_CLOSED:
            break
window.read()
window.close()





