import constants as const

import hotkeymgr as hk
import farmScriptState as st

# Create a shared (global) state
globalState = st.appState()

import routines  # routines depends on the global state so the import is after (FIX THIS AFTER)


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
        and globalState.selectedResource != None
        and globalState.selectedZone != None
        and globalState.selectedKey != None
    ):
        hotkeyListener.startScript()
        newStatus = const.STATUS_ACTIVE

        window["text_status"].update(
            newStatus, text_color="#000000", background_color="#50C878"
        )
        globalState.status = newStatus

        window["combo_key"].update(disabled=True)
        globalState.isKeyComboEnabled = False

        startSelectedScript()

        # disable start
        window["button_start"].update(disabled=True)
        globalState.isStartButtonEnabled = False

        # enable stop
        window["button_stop"].update(disabled=False)
        globalState.isStopButtonEnabled = True
        
    print(globalState)

def onClick_Stop_Button(e, values, window):
    hotkeyListener.stopScript()
    newStatus = const.STATUS_STOPPED

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

    # enable key combo
    window["combo_key"].update(disabled=False)
    globalState.isKeyComboEnabled = True

    # Clear selected hotkey
    globalHotkeyManager.clearBinding(globalState.selectedKey)


def onChange_Job_Combo(e, values, window):
    selectedJob = values["combo_job"]
    globalState.selectedJob = selectedJob
    if globalState.selectedZone == None:  # Activate Zone combo
        window["combo_zone"].update(disabled=False)
        globalState.isZoneComboEnabled = True

    #######Define the behavior where zone has been selected


def onChange_Zone_Combo(e, values, window):
    selectedZone = values["combo_zone"]
    globalState.selectedZone = selectedZone
    selectedJob = globalState.selectedJob

    ## This should activate resource-combo and load values depending on selected zone

    # ASTRUB ZONE
    if selectedZone == const.ZONE_ASTRUB:
        # MINER
        if selectedJob == const.JOB_MINER:
            window["combo_resource"].update(
                disabled=False, values=const.ZONE_RESOURCES_MINER_ASTRUB
            )
            globalState.isResourceComboEnabled = True

        # FARMER
        if selectedJob == const.JOB_FARMER:
            window["combo_resource"].update(
                disabled=False, values=const.ZONE_RESOURCES_FARMER_ASTRUB
            )
            globalState.isResourceComboEnabled = True
        
        # HERBALIST
        if selectedJob == const.JOB_HERBALIST:
            window["combo_resource"].update(
                disabled=False, values=const.ZONE_RESOURCES_HERBALIST_ASTRUB
            )
            globalState.isResourceComboEnabled = True

    if selectedZone == const.ZONE_WILD_ESTATE:
        # MINER
        if selectedJob == const.JOB_MINER:
            window["combo_resource"].update(
                disabled=False, values=const.ZONE_RESOURCES_MINER_WILDESTATE
            )
            globalState.isResourceComboEnabled = True


def onChange_Resource_Combo(e, values, window):
    selectedResource = values["combo_resource"]
    globalState.selectedResource = selectedResource
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
    # Miner
    zone = globalState.selectedZone
    job = globalState.selectedJob
    if (
        job == const.JOB_MINER
        and (zone == const.ZONE_ASTRUB or zone == const.ZONE_WILD_ESTATE)
        and globalState.selectedKey != None
    ):
        # Bind the action to a hotkey
        globalHotkeyManager.setBinding(
            globalState.selectedKey,
            routines.advanced_mining_actions,  # simple_mining_actions#
        )

    # Farmer
    if (
        globalState.selectedJob == const.JOB_FARMER
        and globalState.selectedZone == const.ZONE_ASTRUB
        and globalState.selectedKey != None
    ):
        # Bind the action to a hotkey
        globalHotkeyManager.setBinding(
            globalState.selectedKey,
            routines.advanced_farming_actions,
        )
    
    # Herbalist
    if (
        globalState.selectedJob == const.JOB_HERBALIST
        and globalState.selectedZone == const.ZONE_ASTRUB
        and globalState.selectedKey != None
    ):
        # Bind the action to a hotkey
        globalHotkeyManager.setBinding(
            globalState.selectedKey,
            routines.advanced_herbalist_actions,
        )

