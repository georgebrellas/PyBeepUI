# PyBeep, the GUI program nobody asked for! Made by George Brellas.
# Frequency range: 37hz - 32767hz (This is a limitation set by the winsound module)
from PySimpleGUI import Button, Column, Slider, Input, Text, Window
from winsound import Beep

col1 = [[Button("Beep!", tooltip="Beeps! :)"),
         Text("Step:", tooltip="Frequency to lower/raise by"),
         Input(default_text="50", do_not_clear=True, key="Step", tooltip="Frequency to lower/raise by", size=(5, 5)),
         Text("MS:", tooltip="Milliseconds to beep for"),
         Input(default_text="1000", do_not_clear=True, key="Time", tooltip="Milliseconds to beep for", size=(5, 5))],
        [Slider(range=(37, 32767), orientation='h', default_value=10000, key="Beep", tooltip="Current frequency")],
        [Button("-", key="Lower", tooltip="Lower frequency", size=(1, 1)),
         Button("+", key="Raise", tooltip="Raise frequency", size=(1, 1))]]

layout = [[Column(col1)]]

window = Window("Beep!").Layout(layout).Finalize()
window.Size = (310, 140)
while True:
    event, values = window.Read(timeout=10)

    if not event or event == "Quit":
        break
    elif event == "Raise":
        window.Element("Beep").Update(values["Beep"] + int(values["Step"]))
    elif event == "Lower":
        window.Element("Beep").Update(values["Beep"] - int(values["Step"]))

    elif event == "Beep!":
        print(values)
        Beep(int(values["Beep"]), int(values["Time"]))
