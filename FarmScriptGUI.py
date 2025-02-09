import PySimpleGUI as sg  # Simple GUI for Python
import core
import guiElements

import constants as const

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 350

# Setup the simple window
sg.theme("Black")


layout = [
    [guiElements.frameSelectJobAndZone],
    [guiElements.frameSelectResource],
    [guiElements.frameAssignAKey],
    [guiElements.layoutStatusAndStartStopBtns],
]


# Create the Window
window = sg.Window(
    title= const.PROJECT_NAME + " " + const.VERSION,
    layout=layout,
    size=(WINDOW_WIDTH, WINDOW_HEIGHT),
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

    if event == "combo_resource":
        core.onChange_Resource_Combo(event, values, window)

    if event == "combo_job":
        core.onChange_Job_Combo(event, values, window)


window.close()
