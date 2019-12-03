import time
from easygopigo3 import EasyGoPiGo3


class LedLightIndicator:
    def __init__(self):
        gpg = EasyGoPiGo3()
        my_led = gpg.init_led("AD1")
        self.led = my_led

    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)