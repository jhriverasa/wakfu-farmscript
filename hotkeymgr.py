from pynput import keyboard


def doNothing():
    pass


F_KEYS = [
    "Key.f1",
    "Key.f2",
    "Key.f3",
    "Key.f4",
    "Key.f5",
    "Key.f6",
    "Key.f7",
    "Key.f8",
    "Key.f9",
    "Key.f10",
]

# It supposed to assign one key to one action (function)
initialKeyBindings = {
    "Key.f1": doNothing,
    "Key.f2": doNothing,
    "Key.f3": doNothing,
    "Key.f4": doNothing,
    "Key.f5": doNothing,
    "Key.f6": doNothing,
    "Key.f7": doNothing,
    "Key.f8": doNothing,
    "Key.f9": doNothing,
    "Key.f10": doNothing,
}


class Singleton(type):  # Singleton Metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Hotkey Manager provides a way to bind a key to a specific action
class HotkeyManager(metaclass=Singleton):
    def __init__(self):
        self.isActive = False
        # Bindings are a dict of actions (callback functions) for every key (f1,f2,f3...)
        self._bindings = initialKeyBindings

    # Replace the current action for a key
    def setBinding(self, key, callback: callable):
        self._bindings[key] = callback

    def clearBinding(self, key):
        self._bindings[key] = doNothing

    # Is a key already bound?
    def isBound(self, key):
        return not (self._bindings[key] is doNothing)

    # Calls the function according to the key pressed
    def runHotkeyCallback(self, key):
        try:
            srtKey = str(key)
            if srtKey in F_KEYS:  # Only accepts F1,f2,f3.... keys
                self._bindings.get(srtKey)()
        except:
            print("ERROR: Run Hotkey callback failed")


## HotkeyListener awaits for a Key (F1,F2,F3...) and performs the appropriate action
## that is, the one bound for the specific key in HotkeyManager._bindings
class HotkeyListener(metaclass=Singleton):
    def __init__(self, hkCallback: callable):
        # hkCallback is the function that decides which action should be performed (HotkeyManager.runHotkeyCallback)
        self.hkCallback = hkCallback
        self.listener = None
        self.isActive = False

    def startScript(self):
        if not self.isActive:
            self.listener = keyboard.Listener(on_release=self.hkCallback)
            self.listener.start()
            self.isActive = True

    def stopScript(self):
        if self.isActive:
            self.listener.stop()
            self.listener = None
            self.isActive = False
