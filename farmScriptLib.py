from pynput import keyboard  # Used to listen to keyboard events (Keylogging)


## Routine Class
class ScriptRoutine:
    def __init__(self, on_press, on_release):
        # Creates the instance of Listener
        self.on_press = on_press
        self.on_release = on_release


## Script Class
class FarmScript:
    def __init__(self, routine: ScriptRoutine):
        # Creates the instance of Listener
        self.routine = routine
        self.listener = None
        self.isActive = False

    def startScript(self):
        if not self.isActive:
            self.listener = keyboard.Listener(
                on_press=self.routine.on_press, on_release=self.routine.on_release
            )
            self.listener.start()
            self.isActive = True

    def stopScript(self):
        if self.isActive:
            self.listener.stop()
            self.listener = None
            self.isActive = False
