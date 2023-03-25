import PySimpleGUI as sg #GUI for Python

import farmScriptLib as fslib


#Setup the simple window
sg.theme('Black')
layout = [ [sg.Text(text='Status: Waiting...',enable_events=True,key="text_status"), 
            sg.Button('Start (F1)',key='button_start'), 
            sg.Button('Stop (F2)',key='button_stop')]]


#mouse = Controller()

# Create the Window
window = sg.Window(title='Wakfu FarmBot 0.1', 
                   layout=layout,
                   size=(275,50), 
                   element_justification='c')

#Instance a new Farm Script
farmer = fslib.farmScript(on_press=fslib.farm_on_press,
                          on_release=fslib.farm_on_release)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes windows   
        break

    if event == 'button_start': 
        farmer.startScript()
        window['text_status'].update('ACTIVE',text_color="#000000", background_color='#50C878')
    if event == 'button_stop': 
        farmer.stopScript()
        window['text_status'].update('STOPPED',text_color="#000000", background_color='#C70039')
        

window.close()