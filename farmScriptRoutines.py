#########################  TWEENING  #####################################
##    pyautogui.easeInQuad   ->    Start slow, end fast
##    pyautogui.easeOutQuad   ->   Start fast, end slow
##    pyautogui.easeInOutQuad ->   Start and end fast, slow in middle
##    pyautogui.easeInBounce  ->   Bounce at the end
##    pyautogui.easeInElastic ->   Rubber band at the end

import time
import pyautogui as auto  ##Allows to control mouse + keyboard

from farmScriptLib import ScriptRoutine


screenResX, screenResY = auto.size()


def mining_steps():
    # Simple right click (press+release)
    auto.rightClick(interval=0.125)
    time.sleep(0.2)

    # move pointer and click again
    curPosX, curPosY = auto.position()
    auto.moveTo(curPosX, curPosY - 48, 0.125)

    auto.leftClick(duration=0.1)


def mining_on_press(key):
    return


def mining_on_release(key):
    try:
        if str(key) == "Key.f2":
            mining_steps()
    except:
        print("ERROR ON_RELEASE")


########################################################################
############################### ROUTINES  ##############################
########################################################################

mining_routine = ScriptRoutine(on_press=mining_on_press, on_release=mining_on_release)
