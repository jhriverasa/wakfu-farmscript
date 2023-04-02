# Wakfu Farmbot 0.1

## Description
A "quite simple" Python script that allows to detect and harvest resources on screen, not intended like a bot but a semi-automated tool that performs some clicks over the correct place. 

## Farmbot? ... No, Farmscript, this is not meant for AFK farming 
Tool does not have any feature for AFK farming, that would damage game economy.
Despite of its name is Farmbot, this is just a script for click automation.

## How does this actually work?
Well, basically script takes a screenshot and tries to find an image in it ([ Object detection ](https://www.mathworks.com/discovery/object-detection.html)). If an image/resource is detected clicks on it, detect the icon to harvest and clicks one more time. Really simple

## Requirements
1. Install Python 3 
2. Use a package installer like PIP and use it for install:
    * PySimpleGUI ->  `pip install pyautogui`
    * pyautogui  ->  `pip install pysimplegui`
    * Pillow -> `pip install Pillow`
    * opencv-python -> `pip install opencv-python`
    * pynput -> `pip install pynput`
3. Open ``run.cmd`` 

## How to use
TODO



