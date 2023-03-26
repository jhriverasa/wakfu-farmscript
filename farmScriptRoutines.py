#########################  TWEENING  #####################################
##    pyautogui.easeInQuad   ->    Start slow, end fast
##    pyautogui.easeOutQuad   ->   Start fast, end slow
##    pyautogui.easeInOutQuad ->   Start and end fast, slow in middle
##    pyautogui.easeInBounce  ->   Bounce at the end
##    pyautogui.easeInElastic ->   Rubber band at the end

import time
import math
import pyautogui as auto  ##Allows to control mouse + keyboard

from farmScriptLib import ScriptRoutine

screenResX, screenResY = auto.size()
IMG_PATH = "img" + "\\"


def getClosestPoint(pointlist):
    ##Since the character is always in the "center of the screen" when you're moving
    ## is possible to approximate the distance to resource and improve the harvesting route
    # A long distance (distance of the diagonal in pixels)
    shortestDistance = math.dist([0, screenResY], [screenResX, 0])
    closestPoint = None
    centerOfScreen = [int(screenResX / 2), int(screenResY / 2)]

    for point in pointlist:
        curDistance = math.dist(centerOfScreen, auto.center(point))
        if curDistance < shortestDistance:
            shortestDistance = curDistance
            closestPoint = point

    return auto.center(closestPoint)


###-----------------Simple Mining-------------------->
def simple_mining_steps():
    # Simple right click (press+release)
    auto.rightClick(interval=0.125)
    time.sleep(0.2)

    # move pointer and click again
    curPosX, curPosY = auto.position()
    auto.moveTo(curPosX, curPosY - 48, 0.125)

    auto.leftClick(duration=0.1)


def simple_mining_on_press(key):
    return


def simple_mining_on_release(key):
    try:
        if str(key) == "Key.f2":
            simple_mining_steps()
    except:
        print("ERROR ON_RELEASE")


###----------------Advanced Mining------------------------>
def advanced_mining_steps():
    # Locate all ores
    oreLocations = auto.locateAllOnScreen(
        IMG_PATH + "x.png", confidence=0.86
    )  # Based on practical results 0.86 of confidence performs really well


    oreLocations = list(oreLocations)

    if len(oreLocations) > 0:
        closestPoint = getClosestPoint(oreLocations)
        auto.moveTo(closestPoint.x, closestPoint.y)
         # Simple right click (press+release)
        auto.rightClick(interval=0.125)
        time.sleep(0.5)

        # move pointer and click again
        collectIconLocation = auto.locateCenterOnScreen(
            IMG_PATH + "minning-collect-icon.png", confidence=0.97
        )
        if collectIconLocation != None:
            auto.moveTo(collectIconLocation.x, collectIconLocation.y)
            auto.leftClick(duration=0.1)
        else:
            print("Collect Icon not found")
    else:
        print("Ore not found")

   


def advanced_mining_on_press(key):
    return


def advanced_mining_on_release(key):
    try:
        if str(key) == "Key.f2":
            advanced_mining_steps()
    except:
        print("ERROR ON_RELEASE")


########################################################################
############################### ROUTINES  ##############################
########################################################################
simple_mining_routine = ScriptRoutine(
    on_press=simple_mining_on_press, on_release=simple_mining_on_release
)
advanced_mining_routine = ScriptRoutine(
    on_press=advanced_mining_on_press, on_release=advanced_mining_on_release
)