# Application of To Do App
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is ", now)

while True:
    user_action: str = input ("Type add , show, edit,complete or exit:")

    user_action = user_action.strip ()
    # Adding a Todo

    if user_action.startswith ("add"):
        todo = user_action[4:]

        todos = functions.get_todos ()
        todos.append (todo + '\n')

        functions.write_todos (todos_arg=todos, filepath="todos.txt")
    # Showing a Todo

    elif user_action.startswith ("show"):

        todos = functions.get_todos ()

        for index, items in enumerate (todos):
            items = items.strip ('\n')
            row = f"{index + 1}-{items}"
            print (row)
    # Editing A Todo

    elif user_action.startswith ("edit"):
        try:
            number = int (user_action[5:])
            print (number)
            number = number - 1

            todos = functions.get_todos ()

            new_todo = input ("Enter a New todo:")
            todos[number] = new_todo + "\n"

            functions.write_todos (todos_arg=todos, filepath="todos.txt")

        except ValueError:
            print ("Command is not valid !!!")
            continue
    # Complete a Task in Todo

    elif user_action.startswith ("complete"):
        try:
            number = int (user_action[9:])

            todos = functions.get_todos ()

            index = number - 1
            todo_to_remove = todos[index].strip ("\n")
            todos.pop (index)

            functions.write_todos (todos_arg=todos, filepath="todos.txt")

            message = f"Todo {todo_to_remove} was removed.."
            print (message)

        except IndexError:
            print ("There is No Item in this Index!!")
            continue
# Exiting the Todo App
    elif user_action.startswith ("exit"):
        break

    else:
        print ("Not Valid command!!")
print ('Bye')
