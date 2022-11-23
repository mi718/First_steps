import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
label2 = sg.Text("Select destination folder:")
input_box1 = sg.InputText(tooltip="")
input_box2 = sg.InputText(tooltip="")
button_chose1 = sg.FileBrowse("Chose")
button_chose2 = sg.FileBrowse("Chose")
button_chose3 = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[[label1, input_box1, button_chose1],
                                          [label2, input_box2, button_chose2],
                                          [button_chose3]])
window.read()
window.close()
