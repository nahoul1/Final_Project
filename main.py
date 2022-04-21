from Fix_Words import Modify
import PySimpleGUI as sg

# creates window
layout = [
        [sg.Text('Spell Checker')],
        [sg.Text("Enter the name of the text file you want to check:"), sg.Input()],
        [sg.Submit("Submit")]
        ]

window = sg.Window("Spell Checker", layout,)
event, values = window.read()
print("The original is: ")

Modify.original(values[0])
Modify.check(values[0])
