# To-do app
todos = []

while True:
    user_action = input("Type add or show or exit:")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter Todo:")
            todos.append(todo)

        case "show":
            print(todos)

        case "exit":
            break

print("Bye")

