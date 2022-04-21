from Fix_Words import Modify
import PySimpleGUI as sg


# creates window
layout = [
        [sg.Text("                Spell Checker: ")],
        [sg.Text("Please enter the name of the .txt textfile", size=(30, 1)), sg.InputText()],
        [sg.Submit()]
        ]
sg.theme('BlueMono')
window = sg.Window("Spell Checker", layout,)
event, values = window.read()
window.close()


print("The original text is: ")
Modify.original(values[0])

Modify.check(values[0])
