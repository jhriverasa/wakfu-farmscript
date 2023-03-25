from pynput.mouse import Button as mb, Controller as mc  #Allows to control mouse
from pynput import  keyboard #used to listen keyboard events
import time

#mouseController
mouse = mc()


def farm_routine():
   #Simple right click (press+release)
    mouse.click(mb.right)
    mouse.release(mb.right)
    time.sleep(0.65)

    #move pointer and click again
    curPosX, curPosY = mouse.position
    mouse.position = (curPosX, curPosY-48)
    time.sleep(0.2)
    mouse.click(mb.left)
    #mouse.release(mb.left)


def farm_on_press(key):
    return

def farm_on_release(key):
    try:
        if str(key) == "Key.f2":
            farm_routine()
    except:
        print('ERROR ON_RELEASE')


## Use the class and start/stop methods of Listener outside
class farmScript():

    def __init__(self, on_press, on_release):
        #Creates the instance of Listener
        self.listener = None
        self.on_press= on_press
        self.on_release = on_release
        self.isActive = False

    def startScript(self):
        self.listener = keyboard.Listener(on_press=farm_on_press, on_release=farm_on_release)
        self.listener.start()
        
    def stopScript(self):
        self.listener.stop()
        self.listener = None
        











