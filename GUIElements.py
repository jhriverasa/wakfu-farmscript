import PySimpleGUI as sg  # Simple GUI for Python

import Constants as cts

sg.theme("Black")




frameSelectJobAndZone = sg.Frame(
    title="< Select profession and Zone >",
    layout=[
        [
            sg.Combo(
                values=[
                    cts.CONST_JOB_MINER,
                    cts.CONST_JOB_LUMBERJACK,
                    cts.CONST_JOB_FARMER,
                    cts.CONST_JOB_FISHERMAN,
                    cts.CONST_JOB_HERBALIST,
                    cts.CONST_JOB_TRAPPER,
                ],
                readonly=True,
                enable_events=True,
                key="combo_job",
            ),
            sg.Combo(
                values=[
                    cts.CONST_ZONE_ASTRUB,
                    cts.CONST_ZONE_AMAKNA,
                    cts.CONST_ZONE_BRAKMAR,
                ],
                readonly=True,
                enable_events=True,
                key="combo_zone",
            ),
        ]
    ],
)

frameAssignAKey = sg.Frame(
    title="< Assign a key >",
    layout=[
        [
            sg.Combo(
                values=[
                    cts.CONST_KEY_STR_F1,
                    cts.CONST_KEY_STR_F2,
                    cts.CONST_KEY_STR_F3,
                    cts.CONST_KEY_STR_F4,
                    cts.CONST_KEY_STR_F5,
                    cts.CONST_KEY_STR_F6,
                    cts.CONST_KEY_STR_F7,
                ],
                readonly=True,
                enable_events=True,
                key="combo_key",
            ),
        ]
    ],
)

layoutStatusAndStartStopBtns = (
    [
        sg.Text(text=cts.CONST_STATUS_WAITING, enable_events=True, key="text_status"),
        sg.Button("Start", key="button_start"),
        sg.Button("Stop", key="button_stop"),
    ],
)
