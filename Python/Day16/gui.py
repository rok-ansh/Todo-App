import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do List",
                   layout=[[label], [input_box, add_button], [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
