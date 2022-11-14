import functions
import PySimpleGUI as sgui
import time
import os

if not os.path.exists("todox.txt"):
    with open("todos.txt", "w") as file:
        pass

sgui.theme("DarkTeal9")
TIME_FORMAT = "%b/%d/%Y %H:%M:%S"
clock = sgui.Text('', key="clock")
label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter todo", key="todo")
add_button = sgui.Button("Add", size=10, tooltip="Add Todo", key="Add")
#add_button = sgui.Button(size=2, image_source="images/enter.png", mouseover_colors="LightBlue2")
list_box = sgui.Listbox(values=functions.get_todos(), key='todos',
                        enable_events=True, size=[45, 10])
edit_button = sgui.Button("Edit")
complete_button = sgui.Button("Complete")
exit_button = sgui.Button("Exit")

window = sgui.Window('My To-Do App',
                     layout=[[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                     font=('Helvetica', 15))
while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime(TIME_FORMAT))
    # print(event)
    # print(values)
    # print(values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sgui.popup("Please select an item in the list first.", font=('Helvetica', 15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sgui.popup("Please select an item in the list first.", font=('Helvetica', 15))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sgui.WIN_CLOSED:
            break


window.close()