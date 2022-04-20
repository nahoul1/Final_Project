import PySimpleGUI as sg
from Fix_Words import Modify

# create dictionary with every word and cross-check words with
layout = [
        [sg.Text("                Spell Checker: ", size=(30, 3))],
        [sg.Text("Please enter the name of the .txt textfile", size=(30, 1)), sg.InputText()],
        [sg.Submit()]
        ]
sg.theme('BlueMono')
window = sg.Window("Spell Checker", layout, margins=(150, 150))
event, values = window.read()

k = Modify.original(values[0])
w = Modify.check(values[0])

sg.Window(k, layout=[[]], margins=(150, 150)).read()
