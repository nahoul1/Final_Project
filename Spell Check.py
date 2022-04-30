from Fix_Words import Modify, Behold
from GUI import GUI

# opens window to type in text file
values = GUI.open()

run = True
while run:

    try:
        # displays original text
        print("The original text is: ")

        f = Modify(values[0])
        file = Behold(values[0])
        Behold.original(file)

        # spell checks and offers suggestions
        Modify.check(f)
        run = False

    except FileNotFoundError:
        print("Non-existent")
        values = GUI.open()
