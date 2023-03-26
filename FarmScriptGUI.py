import PySimpleGUI as sg  # Simple GUI for Python

#### SHOULD NOT ALLOW TO CLICK START WHEN ACTIVE..

import hotkeymgr as hk
from routines import advanced_mining_actions
import GUIElements
import FarmScriptState as st
import Constants as cts


# Instance HotkeyManager and its correponding Listener
globalHotkeyManager = hk.HotkeyManager()
hotkeyListener = hk.HotkeyListener(globalHotkeyManager.runHotkeyCallback)

# Create the global state
appState = st.appState()

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
        # is everything selected?
        if (
            appState.selectedJob != None
            and appState.selectedKey != None
            and appState.selectedZone != None
        ):
            hotkeyListener.startScript()
            newStatus = cts.CONST_STATUS_ACTIVE
            window["text_status"].update(
                newStatus, text_color="#000000", background_color="#50C878"
            )
            appState.status = newStatus
            print(appState)
            if (
                appState.selectedJob == cts.CONST_JOB_MINER
                and appState.selectedZone == cts.CONST_ZONE_ASTRUB
                and appState.selectedKey != None
            ):
                # Bind the action to a hotkey
                globalHotkeyManager.setBinding(
                    appState.selectedKey, advanced_mining_actions
                )

    if event == "button_stop":
        hotkeyListener.stopScript()
        newStatus = cts.CONST_STATUS_STOPPED
        window["text_status"].update(
            newStatus, text_color="#000000", background_color="#C70039"
        )
        appState.status = newStatus
        print(appState)

    if event == "combo_key":
        selectedHotkey = values["combo_key"]
        appState.selectedKey = selectedHotkey
        print(appState)

    if event == "combo_zone":
        selectedZone = values["combo_zone"]
        appState.selectedZone = selectedZone
        print(appState)

    if event == "combo_job":
        selectedJob = values["combo_job"]
        appState.selectedJob = selectedJob
        print(appState)


window.close()
