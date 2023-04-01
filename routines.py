#########################  TWEENING  #####################################
##    pyautogui.easeInQuad   ->    Start slow, end fast
##    pyautogui.easeOutQuad   ->   Start fast, end slow
##    pyautogui.easeInOutQuad ->   Start and end fast, slow in middle
##    pyautogui.easeInBounce  ->   Bounce at the end
##    pyautogui.easeInElastic ->   Rubber band at the end

import time
import math
import random
import pyautogui as auto  ##Allows to control mouse + keyboard
from core import globalState
import constants as const

screenResX, screenResY = auto.size()


########################################################################
######################## HELPER FUNCTIONS ##############################
########################################################################
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


def getImgNameFromResourceConst(resConst: str, subcategory: str = ""):
    ## subcategory is just a string that is added before extension
    ## useful when resource has 2 differen types of images depending on the current state (Lumberjack / Farmer)
    if subcategory != "":
        subcategory = "-" + subcategory

    return resConst.replace(" ", "-") + subcategory + ".png"


def tossACoin(chanceEventA: float = 0.5):
    if random.random() >= chanceEventA:
        return False  #'Heads'
    else:
        return True  #'Tails'


def moveAndClickLocation(x: int, y: int, button: str = "left", sleepTime: float = 0.15):
    auto.moveTo(x, y)

    if button == "left":
        auto.leftClick()
    elif button == "right":
        auto.rightClick()
    elif button == "middle":
        auto.middleClick()
    else:
        print("WRONG PARAMETER")
    time.sleep(sleepTime)


def findIconAndClick(iconPath: str, confidence: float = 0.97, duration: float = 0.1):
    ret = False
    collectIconLocation = auto.locateCenterOnScreen(
        const.ICONS_PATH + iconPath, confidence=confidence
    )
    if collectIconLocation != None:
        auto.moveTo(collectIconLocation.x, collectIconLocation.y)
        auto.leftClick(duration=duration)
        # returns False if icon was found
        ret = True

    return ret


def getActionIconByResource(job: str, constResourceName: str, action: str):
    if job == const.CONST_JOB_FARMER:
        # actions for farmer: ["harvest", "seeds"]
        return const.CONST_ICON_FOR_ACTIONS_FARMER.get(constResourceName).get(action)


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
        const.ICONS_PATH + const.CONST_ICON_ACTION_MINING_HARVEST, confidence=0.97
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
        const.MINER_RES_PATH
        + getImgNameFromResourceConst(globalState.selectedResource),
        confidence=0.86,
    )  # Based on practical results 0.86 of confidence performs really well

    oreLocations = list(oreLocations)

    if len(oreLocations) > 0:
        closestPoint = getClosestPoint(oreLocations)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")

        if not findIconAndClick(iconPath=const.CONST_ICON_ACTION_MINING_HARVEST):
            print("Minning Icon not found")
    else:
        print("Resource not found")


def advanced_farming_actions():
    selectedResource = globalState.selectedResource
    # Check if harvesting seeds is possible
    seedsLocation = auto.locateAllOnScreen(
        const.FARMER_RES_PATH
        + getImgNameFromResourceConst(selectedResource, subcategory="seed"),
        confidence=0.80,  # Need to be tuned
    )

    # Locate all resources
    resourceLocation = auto.locateAllOnScreen(
        const.FARMER_RES_PATH + getImgNameFromResourceConst(selectedResource),
        confidence=0.80,  # Need to be tuned
    )

    # Cast Generator into a List
    seedsLocation = list(seedsLocation)
    resourceLocation = list(resourceLocation)

    # Switch-like (by cases) treatment
    closestPoint = None  # Just a definition
    if len(seedsLocation) > 0 and len(resourceLocation) > 0:
        if tossACoin(0.66):  # Gonna get resources  2 out 3 times
            closestPoint = getClosestPoint(seedsLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            findIconAndClick(
                iconPath=getActionIconByResource(
                    const.CONST_JOB_FARMER, selectedResource, "seeds"
                )
            )
        else:
            closestPoint = getClosestPoint(resourceLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            findIconAndClick(
                iconPath=getActionIconByResource(
                    const.CONST_JOB_FARMER, selectedResource, "harvest"
                )
            )
    elif len(seedsLocation) > 0 and len(resourceLocation) == 0:
        closestPoint = getClosestPoint(seedsLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        findIconAndClick(
            iconPath=getActionIconByResource(
                const.CONST_JOB_FARMER, selectedResource, "seeds"
            )
        )
    elif len(seedsLocation) == 0 and len(resourceLocation) > 0:
        closestPoint = getClosestPoint(resourceLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        findIconAndClick(
            iconPath=getActionIconByResource(
                const.CONST_JOB_FARMER, selectedResource, "harvest"
            )
        )
        print("Seeds Not Found")
    else:
        print("Resource not found")
