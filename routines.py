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


def findIconAndClick(constIcon: str, confidence: float = 0.96, duration: float = 0.1):
    ret = False
    collectIconLocation = auto.locateCenterOnScreen(
        const.ICONS_PATH + constIcon, confidence=confidence
    )
    if collectIconLocation != None:
        auto.moveTo(collectIconLocation.x, collectIconLocation.y)
        auto.leftClick(duration=duration)
        # returns False if icon was found
        ret = True

    return ret


def getActionIconByResource(job: str, constResourceName: str, action: str):
    if job == const.JOB_FARMER:
        # actions for farmer: ["harvest", "seeds"]
        return const.ICON_FOR_ACTIONS_FARMER.get(constResourceName).get(action)


########################################################################
############################### ROUTINES  ##############################
########################################################################


###-----------------Simple Routines-------------------->
def simple_mining_actions():
    auto.rightClick(duration=0.2)
    wasIconFound = findIconAndClick(constIcon=const.ICON_ACTION_MINING_HARVEST)
    print("Found Minning icon" if wasIconFound else "Icon was not found")


def simple_trapper_actions():
    auto.rightClick(duration=0.2)
    if tossACoin(0.55):  ## 55% of times
        findIconAndClick(constIcon=const.ICON_ACTION_TRAPPER_SEEDS)
    else:
        findIconAndClick(constIcon=const.ICON_ACTION_FARMING_SEEDS)
        


###----------------Advanced Routines------------------------>
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

        if not findIconAndClick(constIcon=const.ICON_ACTION_MINING_HARVEST):
            print("Minning Icon not found")
    else:
        print("Resource not found")


def advanced_fisherman_actions():
    accuracy = 0.88

    # Locate all
    fishLocationsPos1 = auto.locateAllOnScreen(
        const.FISHERMAN_RES_PATH + "fish1.png",
        confidence=accuracy,
    )
    fishLocationsPos2 = auto.locateAllOnScreen(
        const.FISHERMAN_RES_PATH + "fish2.png",
        confidence=accuracy,
    )
    fishLocationsPos3 = auto.locateAllOnScreen(
        const.FISHERMAN_RES_PATH + "fish3.png",
        confidence=accuracy,
    )
    fishLocationsPos4 = auto.locateAllOnScreen(
        const.FISHERMAN_RES_PATH + "fish4.png",
        confidence=accuracy,
    )
    fishLocations = (
        list(fishLocationsPos1)
        + list(fishLocationsPos2)
        + list(fishLocationsPos3)
        + list(fishLocationsPos4)
    )

    if len(fishLocations) > 0:
        closestPoint = getClosestPoint(fishLocations)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")

        if not findIconAndClick(constIcon=const.ICON_ACTION_FISHERMAN_FISH):
            print("Fishing Icon not found")
    else:
        print("Fishes not found")


def advanced_farming_actions():
    selectedResource = globalState.selectedResource
    # Check if harvesting seeds is possible
    seedsLocation = auto.locateAllOnScreen(
        const.FARMER_RES_PATH
        + getImgNameFromResourceConst(selectedResource, subcategory="seed"),
        confidence=0.75,  # Need to be tuned
    )

    # Locate all resources
    resourceLocation = auto.locateAllOnScreen(
        const.FARMER_RES_PATH + getImgNameFromResourceConst(selectedResource),
        confidence=0.75,  # Need to be tuned
    )

    # Cast Generator into a List
    seedsLocation = list(seedsLocation)
    resourceLocation = list(resourceLocation)

    # Switch-like (by cases) treatment
    closestPoint = None  # Just a definition
    totalSeedsFound = len(seedsLocation)
    totalResourcesFound = len(resourceLocation)
    if totalSeedsFound > 0 and totalResourcesFound > 0:
        if tossACoin(0.5):
            closestPoint = getClosestPoint(seedsLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            # This need to be tuned so that it has a balance point between seeds - resource
            findIconAndClick(
                constIcon=getActionIconByResource(
                    const.JOB_FARMER,
                    selectedResource,
                    "harvest" if tossACoin(0.65) and totalSeedsFound > 1 else "seeds",
                )
            )
        else:
            closestPoint = getClosestPoint(resourceLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            findIconAndClick(
                constIcon=getActionIconByResource(
                    const.JOB_FARMER, selectedResource, "harvest"
                )
            )
    elif totalSeedsFound > 0 and totalResourcesFound == 0:
        closestPoint = getClosestPoint(seedsLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        findIconAndClick(
            constIcon=getActionIconByResource(
                const.JOB_FARMER, selectedResource, "seeds"
            )
        )
    elif totalSeedsFound == 0 and totalResourcesFound > 0:
        closestPoint = getClosestPoint(resourceLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        findIconAndClick(
            constIcon=getActionIconByResource(
                const.JOB_FARMER, selectedResource, "harvest"
            )
        )
        print("Seeds Not Found")
    else:
        print("Resource not found")


def advanced_lumberjack_actions():
    # TODO Trees change its model so resource images like  Birch and Boabob do not take this into account, Update for
    # more universal image or design a strategy to contemplate this possibility

    # Some trees has an aditional resource (for instance apples from Api tree) in its mature state
    # So this should check if the aditional resource is available by checking the "get icon"

    selectedResource = globalState.selectedResource
    # Check the mature version
    matureTreeLocation = auto.locateAllOnScreen(
        const.LUMBERJACK_RES_PATH
        + getImgNameFromResourceConst(selectedResource, subcategory="mature"),
        confidence=0.88,  # Need to be tuned
    )

    # Locate all resources
    littleTreeLocation = auto.locateAllOnScreen(
        const.LUMBERJACK_RES_PATH + getImgNameFromResourceConst(selectedResource),
        confidence=0.88,  # Need to be tuned
    )

    # Cast Generator into a List
    matureTreeLocation = list(matureTreeLocation)
    littleTreeLocation = list(littleTreeLocation)

    # Switch-like (by cases) treatment
    closestPoint = None  # Just a definition
    totalMatureTreesFound = len(matureTreeLocation)
    totalLittleTreesFound = len(littleTreeLocation)
    if totalMatureTreesFound > 0 and totalLittleTreesFound > 0:
        if tossACoin(0.7):
            closestPoint = getClosestPoint(matureTreeLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            # try to get secondary resource first
            gotSecondaryRes = findIconAndClick(
                constIcon=const.ICON_ACTION_LUMBERJACK_GET
            )
            if not gotSecondaryRes:
                findIconAndClick(constIcon=const.ICON_ACTION_LUMBERJACK_CUT_TREE)
        else:
            closestPoint = getClosestPoint(littleTreeLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            # get cuttings
            findIconAndClick(constIcon=const.ICON_ACTION_FARMING_CUT)

    elif totalMatureTreesFound > 0 and totalLittleTreesFound == 0:
        closestPoint = getClosestPoint(matureTreeLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        # try to get secondary resource first
        gotSecondaryRes = findIconAndClick(constIcon=const.ICON_ACTION_LUMBERJACK_GET)
        if not gotSecondaryRes:
            findIconAndClick(constIcon=const.ICON_ACTION_LUMBERJACK_CUT_TREE)

    elif totalMatureTreesFound == 0 and totalLittleTreesFound > 0:
        closestPoint = getClosestPoint(littleTreeLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        # get cuttings
        findIconAndClick(constIcon=const.ICON_ACTION_FARMING_CUT)
        print("Cuttings Not Found")
    else:
        print("Lumberjack Res not found")


def advanced_herbalist_actions():
    selectedResource = globalState.selectedResource
    # Check if harvesting seeds is possible
    seedsLocation = auto.locateAllOnScreen(
        const.HERBALIST_RES_PATH
        + getImgNameFromResourceConst(selectedResource, subcategory="seed"),
        confidence=0.82,  # Need to be tuned
    )

    # Locate all resources
    resourceLocation = auto.locateAllOnScreen(
        const.HERBALIST_RES_PATH + getImgNameFromResourceConst(selectedResource),
        confidence=0.82,  # Need to be tuned
    )

    # Cast Generator into a List
    seedsLocation = list(seedsLocation)
    resourceLocation = list(resourceLocation)

    # Switch-like (by cases) treatment
    closestPoint = None  # Just a definition
    totalSeedsFound = len(seedsLocation)
    totalResourcesFound = len(resourceLocation)
    if totalSeedsFound > 0 and totalResourcesFound > 0:
        if tossACoin(0.66):
            closestPoint = getClosestPoint(seedsLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            # This need to be tuned so that it has a balance point between seeds - resource
            prob = tossACoin(0.25)
            print(
                "found seeds and resource: "
                + ("cutting..." if prob else "getting seeds...")
            )
            findIconAndClick(
                # 32% of chance of not getting seeds but get the resource
                constIcon=(
                    const.ICON_ACTION_HERBALIST_CUT
                    if prob and totalSeedsFound > 1
                    else const.ICON_ACTION_HERBALIST_SEEDS
                )
            )
        else:
            closestPoint = getClosestPoint(resourceLocation)
            moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
            findIconAndClick(constIcon=(const.ICON_ACTION_HERBALIST_CUT))
            print("found seeeds and resourcer, trying to cut...")
    elif totalSeedsFound > 0 and totalResourcesFound == 0:
        closestPoint = getClosestPoint(seedsLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        if tossACoin(0.66): 
            findIconAndClick(constIcon=(const.ICON_ACTION_HERBALIST_SEEDS))
        else:
            findIconAndClick(constIcon=(const.ICON_ACTION_HERBALIST_CUT))
        print("only found seeds")
    elif totalSeedsFound == 0 and totalResourcesFound > 0:
        closestPoint = getClosestPoint(resourceLocation)
        moveAndClickLocation(closestPoint.x, closestPoint.y, "right")
        findIconAndClick(constIcon=(const.ICON_ACTION_HERBALIST_CUT))
        print("Seeds were not found")
    else:
        print("Herbalist Resource not found")
