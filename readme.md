
# Wakfu Farmbot (Still under development)

## Description
A Python script that allows to detect and harvest resources on screen, not intended like a bot but a semi-automated tool that performs some clicks over the correct place.


## Farmbot? ... No, Farmscript, this is not meant for AFK farming

Tool does not have any feature for AFK farming, that would damage game economy.
Despite of its name is Farmbot, this is just a script for click automation.

  
## How does this actually work?

Well, basically script takes a screenshot and tries to find an image in it ([ Object detection ](https://www.mathworks.com/discovery/object-detection.html)). If an image/resource is detected clicks on it, detect the icon to harvest and clicks one more time. Really simple


## Requirements
**1.** Install Python 3
**2.** Use a package installer like PIP and use it for install:
* PySimpleGUI -> `pip install pyautogui`
* pyautogui -> `pip install pysimplegui`
* Pillow -> `pip install Pillow`
* opencv-python -> `pip install opencv-python`
* pynput -> `pip install pynput`

**3.** Open ``run.cmd``

  

## How many professions supports, how efficient is it?

Every profession related to harvest/ get some stuff:

* **Miner** -> 95%
* **Lumberjack** -> 85%
* **Farmer** -> 70%
* **Fisherman** -> 50%
* **Herbalist** -> 65%
* **Trapper** -> 100% (It does not detect anything you point, it just clicks and selects the icon )

1) *Percentages presented above correspond to experimental results, basically tells you how accurate is when detecting resources*
2) In each category (Jobs), the specific resource is detected with a different accuracy, for example:  Detecting Babbage Plant is way easier than detecting Wheat, Why? Small object detection is not easy to approach (https://blog.roboflow.com/detect-small-objects/) and decreasing accuracy leads to increase false positives. 
3) Despite of that ↑ is really good finding resources like trees, ores, big plants etc

**TLDR:** Sometimes work, sometimes does not :v 

## Ok, so... can I use it now?

**Short answer:** Nope 😎
**Detailed answer:** Tecnically, yes, but you have to reproduce all the conditions (environment) that is being used for development, not a big deal but at least 10 steps. 

## A demo!
- Late May 2023
