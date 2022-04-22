import PySimpleGUI as sg


class GUI:

    @staticmethod
    def open():
        # creates window
        layout = [
            [sg.Text("                Spell Checker: ")],
            [sg.Text("Please enter the name of the .txt textfile", size=(30, 1)), sg.InputText()],
            [sg.Submit()]
        ]
        sg.theme('BlueMono')
        window = sg.Window("Spell Checker", layout, )
        event, values = window.read()
        window.close()
        return values
