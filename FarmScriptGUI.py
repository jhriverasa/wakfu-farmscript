import PySimpleGUI as sg  # Simple GUI for Python

import GUIElements
import Constants as const
import core


# Setup the simple window
sg.theme("Black")


layout = [
    [GUIElements.frameSelectJobAndZone],
    [GUIElements.frameAssignAKey],
    [GUIElements.layoutStatusAndStartStopBtns],
]


# Create the Window
window = sg.Window(
    title="Wakfu FarmBot 0.1",
    layout=layout,
    size=(400, 300),
    element_justification="c",
    element_padding=10,
)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes windows
        break

    if event == "button_start":
        core.onClick_Start_Button(event, values, window)

    if event == "button_stop":
        core.onClick_Stop_Button(event, values, window)

    if event == "combo_key":
        core.onChange_Key_Combo(event, values, window)

    if event == "combo_zone":
        core.onChange_Zone_Combo(event, values, window)
        
    if event == "combo_job":
        core.onChange_Job_Combo(event, values, window)


window.close()
