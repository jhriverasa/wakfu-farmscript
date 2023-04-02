import PySimpleGUI as sg  # Simple GUI for Python
from core import globalState
import constants as const

sg.theme("Black")


frameSelectJobAndZone = sg.Frame(
    title=const.GUI_FRAME_SELECTJOBANDZONE_TEXT,
    expand_x=True,
    layout=[
        [
            sg.Combo(
                values=[
                    const.JOB_MINER,
                    const.JOB_LUMBERJACK,
                    const.JOB_FARMER,
                    const.JOB_FISHERMAN,
                    const.JOB_HERBALIST,
                    const.JOB_TRAPPER,
                ],
                readonly=True,
                expand_x=True,
                enable_events=True,
                key="combo_job",
            ),
            sg.Combo(
                values=[
                    const.ZONE_ASTRUB,
                    const.ZONE_AMAKNA,
                    const.ZONE_BRAKMAR,
                    const.ZONE_WILD_ESTATE
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
    title=const.GUI_FRAME_SELECTRESOURCE_TEXT,
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
    title=const.GUI_FRAME_ASSIGNAKEY,
    expand_x=True,
    layout=[
        [
            sg.Combo(
                values=[
                    const.KEY_STR_F1,
                    const.KEY_STR_F2,
                    const.KEY_STR_F3,
                    const.KEY_STR_F4,
                    const.KEY_STR_F5,
                    const.KEY_STR_F6,
                    const.KEY_STR_F7,
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
        sg.Text(text=const.STATUS_WAITING, enable_events=True, key="text_status"),
        sg.Button(
            const.GUI_BUTTON_START_TEXT,
            disabled=not globalState.isStartButtonEnabled,
            key="button_start",
        ),
        sg.Button(
            const.GUI_BUTTON_STOP_TEXT,
            disabled=not globalState.isStopButtonEnabled,
            key="button_stop",
        ),
    ],
)
