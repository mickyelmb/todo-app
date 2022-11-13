import functions
import PySimpleGUI as sgui

label = sgui.Text("Type in a to-do")
input_box = sgui.InputText(tooltip="Enter todo")
add_button = sgui.Button("Add")

window = sgui.Window('My To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()