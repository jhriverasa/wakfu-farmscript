import PySimpleGUI as sg  # Simple GUI for Python
from core import globalState
import constants as const

sg.theme("Black")


frameSelectJobAndZone = sg.Frame(
    title="< Select profession and Zone >",
    expand_x=True,
    layout=[
        [
            sg.Combo(
                values=[
                    const.CONST_JOB_MINER,
                    const.CONST_JOB_LUMBERJACK,
                    const.CONST_JOB_FARMER,
                    const.CONST_JOB_FISHERMAN,
                    const.CONST_JOB_HERBALIST,
                    const.CONST_JOB_TRAPPER,
                ],
                readonly=True,
                expand_x=True,
                enable_events=True,
                key="combo_job",
            ),
            sg.Combo(
                values=[
                    const.CONST_ZONE_ASTRUB,
                    const.CONST_ZONE_AMAKNA,
                    const.CONST_ZONE_BRAKMAR,
                ],
                readonly=True,
                expand_x=True,
                enable_events=True,
                key="combo_zone",
                disabled=not globalState.isZoneComboEnabled,
            ),
        ]
    ],
)

frameSelectResource = sg.Frame(
    title="< Select resource >",
    expand_x=True,
    layout=[
        [
            sg.Combo(
                values=[],  # This one depends on the zone
                readonly=True,
                enable_events=True,
                key="combo_resource",
                disabled=not globalState.isResourceComboEnabled,
                expand_x=True,
            ),
        ]
    ],
)

frameAssignAKey = sg.Frame(
    title="< Assign a key >",
    expand_x=True,
    layout=[
        [
            sg.Combo(
                values=[
                    const.CONST_KEY_STR_F1,
                    const.CONST_KEY_STR_F2,
                    const.CONST_KEY_STR_F3,
                    const.CONST_KEY_STR_F4,
                    const.CONST_KEY_STR_F5,
                    const.CONST_KEY_STR_F6,
                    const.CONST_KEY_STR_F7,
                ],
                readonly=True,
                enable_events=True,
                key="combo_key",
                disabled=not globalState.isKeyComboEnabled,
            ),
        ]
    ],
)

layoutStatusAndStartStopBtns = (
    [
        sg.Text(text=const.CONST_STATUS_WAITING, enable_events=True, key="text_status"),
        sg.Button(
            "Start", disabled=not globalState.isStartButtonEnabled, key="button_start"
        ),
        sg.Button(
            "Stop", disabled=not globalState.isStopButtonEnabled, key="button_stop"
        ),
    ],
)
