import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
# Creating the list box
list_box = sg.Listbox(functions.get_todos(), key='my_todos_list',
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
window = sg.Window("My To-do List",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button],[exit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['my_todos_list'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['my_todos_list'].update(values=todos)

        case "Edit":
            todo_to_edit = values['my_todos_list'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            # Inorder to update listbox live
            window['my_todos_list'].update(values=todos)

        case "my_todos_list":
            window['todo'].update(value=values['my_todos_list'][0])

        case sg.WIN_CLOSED:
            break

        case "Exit":
            break


window.close()
