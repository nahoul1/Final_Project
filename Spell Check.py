from Fix_Words import Modify
from GUI import GUI

# opens window to type in text file
values = GUI.open()

# displays original text
Modify.original(values[0])

# spell checks and offers suggestions
Modify.check(values[0])
