import function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, button]],
                   font=("Cascadia Code", 10))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todos = value['todo'] + '\n'
            todos.append(new_todos)
            function.write_todos(todos)
        case WIN_CLOSED:
            break

window.close()
