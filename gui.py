import PySimpleGUI as sg  # Simple GUI for Python
import hotkeymgr as hk
from routines import advanced_mining_actions


# Setup the simple window
sg.theme("Black")
layout = [
    [
        sg.Text(text="Status: Waiting...", enable_events=True, key="text_status"),
        sg.Button("Start", key="button_start"),
        sg.Button("Stop", key="button_stop"),
    ]
]

# Create the Window
window = sg.Window(
    title="Wakfu FarmBot 0.1", layout=layout, size=(275, 50), element_justification="c"
)

# Instance HotkeyManager and its correponding Listener
globalHotkeyManager = hk.HotkeyManager()
hotkeyListener = hk.HotkeyListener(globalHotkeyManager.runHotkeyCallback)

# Bind the action to a hotkey
if not globalHotkeyManager.isBound("Key.f2"):
    globalHotkeyManager.setBinding("Key.f2", advanced_mining_actions)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes windows
        break

    if event == "button_start":
        hotkeyListener.startScript()
        window["text_status"].update(
            "ACTIVE", text_color="#000000", background_color="#50C878"
        )
    if event == "button_stop":
        hotkeyListener.stopScript()
        window["text_status"].update(
            "STOPPED", text_color="#000000", background_color="#C70039"
        )


window.close()
