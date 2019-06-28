"this module handles generating beep noises"

class Beeper:
    "This object allows the user to trigger beep sounds"

    def __init__(self, mute=False):
        self.mute = mute

    def beep(self):
        "This method will make a single beep sound"
        if not self.mute:
            print('\a\b', end='')
