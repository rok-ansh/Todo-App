import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's now", now)

while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        user_number = int(user_action[5:])
        number = user_number - 1
        todos = functions.get_todos()
        edit_item = input("Enter the value to edit : ")
        todos[number] = edit_item + '\n'
        functions.write_todos(todos)

    elif user_action.startswith("complete"):
        user_num = int(user_action[9:])
        number = user_num -1
        todos = functions.get_todos()
        item_completed = todos[number]
        todos.remove(item_completed)
        functions.write_todos(todos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Entered keyword is wrong, Kindly enter add, show")

print("Have a Good Day!!")







