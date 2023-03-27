import Constants as const

#### SHOULD NOT ALLOW TO CLICK START WHEN ACTIVE..
import hotkeymgr as hk
import FarmScriptState as st
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
        print(globalState)
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


def onClick_Stop_Button(e, values, window):
    hotkeyListener.stopScript()
    newStatus = const.CONST_STATUS_STOPPED
    window["text_status"].update(
        newStatus, text_color="#000000", background_color="#C70039"
    )
    globalState.status = newStatus
    print(globalState)


def onChange_Key_Combo(e, values, window):
    selectedHotkey = values["combo_key"]
    globalState.selectedKey = selectedHotkey
    print(globalState)


def onChange_Zone_Combo(e, values, window):
    selectedZone = values["combo_zone"]
    globalState.selectedZone = selectedZone
    print(globalState)


def onChange_Job_Combo(e, values, window):
    selectedJob = values["combo_job"]
    globalState.selectedJob = selectedJob
    print(globalState)
