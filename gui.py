import functions
import PySimpleGUI as sgui

label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter todo", key="todo")
add_button = sgui.Button("Add")
list_box = sgui.Listbox(values=functions.get_todos(), key='todos',
                        enable_events=True, size=[45, 10])
edit_button = sgui.Button("Edit")

window = sgui.Window('My To-Do App',
                     layout=[[label], [input_box, add_button],[list_box, edit_button]],
                     font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sgui.WIN_CLOSED:
            break


window.close()