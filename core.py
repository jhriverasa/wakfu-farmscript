import constants as const

import hotkeymgr as hk
import farmScriptState as st
import routines

# Create a shared (global) state
globalState = st.appState()


# Instance HotkeyManager and its correponding Listener
globalHotkeyManager = hk.HotkeyManager()
hotkeyListener = hk.HotkeyListener(globalHotkeyManager.runHotkeyCallback)

#########################################
############ EVENT HANDLERS #############
#########################################


def onClick_Start_Button(e, values, window):
    # is everything selected?
    if (
        globalState.selectedJob != None
        and globalState.selectedKey != None
        and globalState.selectedZone != None
    ):
        hotkeyListener.startScript()
        newStatus = const.CONST_STATUS_ACTIVE

        window["text_status"].update(
            newStatus, text_color="#000000", background_color="#50C878"
        )
        globalState.status = newStatus
        startSelectedScript()

        # disable start
        window["button_start"].update(disabled=True)
        globalState.isStartButtonEnabled = False

        # enable stop
        window["button_stop"].update(disabled=False)
        globalState.isStopButtonEnabled = True


def onClick_Stop_Button(e, values, window):
    hotkeyListener.stopScript()
    newStatus = const.CONST_STATUS_STOPPED

    window["text_status"].update(
        newStatus, text_color="#000000", background_color="#C70039"
    )
    globalState.status = newStatus
    # disable stop
    window["button_stop"].update(disabled=True)
    globalState.isStopButtonEnabled = False

    # enable start
    window["button_start"].update(disabled=False)
    globalState.isStartButtonEnabled = True

    # Clear selected hotkey
    globalHotkeyManager.clearBinding(globalState.selectedKey)


def onChange_Job_Combo(e, values, window):
    selectedJob = values["combo_job"]
    globalState.selectedJob = selectedJob
    if globalState.selectedZone == None:  # Activate Zone combo
        window["combo_zone"].update(disabled=False)
        globalState.isZoneComboEnabled = True


def onChange_Zone_Combo(e, values, window):
    selectedZone = values["combo_zone"]
    globalState.selectedZone = selectedZone
    if globalState.selectedKey == None:  # Activate Key combo
        window["combo_key"].update(disabled=False)
        globalState.isKeyComboEnabled = True


def onChange_Key_Combo(e, values, window):
    selectedHotkey = values["combo_key"]
    globalState.selectedKey = selectedHotkey
    if (  # First time after selected everything
        globalState.isStartButtonEnabled == False
        and globalState.isStopButtonEnabled == False
    ):  # Activate start button
        globalState.isStartButtonEnabled = True
        window["button_start"].update(disabled=False)


#########################################
########## HelperFunctions ##############
#########################################


def startSelectedScript():
    if (
        globalState.selectedJob == const.CONST_JOB_MINER
        and globalState.selectedZone == const.CONST_ZONE_ASTRUB
        and globalState.selectedKey != None
    ):
        # Bind the action to a hotkey
        globalHotkeyManager.setBinding(
            globalState.selectedKey,
            routines.advanced_mining_actions,  # simple_mining_actions#
        )