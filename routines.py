#########################  TWEENING  #####################################
##    pyautogui.easeInQuad   ->    Start slow, end fast
##    pyautogui.easeOutQuad   ->   Start fast, end slow
##    pyautogui.easeInOutQuad ->   Start and end fast, slow in middle
##    pyautogui.easeInBounce  ->   Bounce at the end
##    pyautogui.easeInElastic ->   Rubber band at the end

import time
import math
import pyautogui as auto  ##Allows to control mouse + keyboard
from core import globalState

screenResX, screenResY = auto.size()
IMG_PATH = "img\\"
MINER_RES_PATH = IMG_PATH + "miner_res\\"
ICONS_PATH = IMG_PATH + "icons\\"
FARMER_RES_PATH = IMG_PATH + "farmer_res\\"


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


def getImgNameFromResourceConst(resConst: str):
    return resConst.replace(" ", "-") + ".png"


########################################################################
############################### ROUTINES  ##############################
########################################################################


###-----------------Simple Mining-------------------->
def simple_mining_actions():
    # Simple right click
    auto.rightClick(interval=0.125)
    time.sleep(0.2)

    # move pointer to mining icon and click again
    collectIconLocation = auto.locateCenterOnScreen(
        ICONS_PATH + "minning-collect-icon.png", confidence=0.97
    )
    if collectIconLocation != None:
        auto.moveTo(collectIconLocation.x, collectIconLocation.y)
        auto.leftClick(duration=0.1)
    else:
        print("Collect Icon not found")


###----------------Advanced Mining------------------------>
def advanced_mining_actions():
    # Locate all ores
    oreLocations = auto.locateAllOnScreen(
        MINER_RES_PATH + getImgNameFromResourceConst(globalState.selectedResource),
        confidence=0.86,
    )  # Based on practical results 0.86 of confidence performs really well

    oreLocations = list(oreLocations)

    if len(oreLocations) > 0:
        closestPoint = getClosestPoint(oreLocations)
        auto.moveTo(closestPoint.x, closestPoint.y)
        # Simple right click
        auto.rightClick(interval=0.125)
        time.sleep(0.5)

        # move pointer and click again
        collectIconLocation = auto.locateCenterOnScreen(
            ICONS_PATH + "minning-harvest-icon.png", confidence=0.97
        )
        if collectIconLocation != None:
            auto.moveTo(collectIconLocation.x, collectIconLocation.y)
            auto.leftClick(duration=0.1)
        else:
            print("Minning Icon not found")
    else:
        print("Resource not found")


def advanced_farming_actions():
    # Locate all ores
    resourceLocation = auto.locateAllOnScreen(
        FARMER_RES_PATH + getImgNameFromResourceConst(globalState.selectedResource),
        confidence=0.86,
    )  # Based on practical results 0.86 of confidence performs really well

    resourceLocation = list(resourceLocation)

    if len(resourceLocation) > 0:
        closestPoint = getClosestPoint(resourceLocation)
        auto.moveTo(closestPoint.x, closestPoint.y)
        # Simple right click
        auto.rightClick(interval=0.125)
        time.sleep(0.5)

        # move pointer and click again
        collectIconLocation = auto.locateCenterOnScreen(
            ICONS_PATH + "farming-reap-icon.png", confidence=0.97
        )
        if collectIconLocation != None:
            auto.moveTo(collectIconLocation.x, collectIconLocation.y)
            auto.leftClick(duration=0.1)
        else:
            # Try a different icon (since farming has two possibilities) #CHANGE THIS DISCRIMINATING BY RESOURCE
            collectIconLocation = auto.locateCenterOnScreen(
                ICONS_PATH + "farming-cut-icon.png", confidence=0.97
            )
            if collectIconLocation != None:
                auto.moveTo(collectIconLocation.x, collectIconLocation.y)
                auto.leftClick(duration=0.1)
            else:
                print("Farming Icon not found")

    else:
        print("Resource not found")
