import easygopigo3 as easy
import cv2
import time

TURN_DISTANCE = 20
TURN_DEGREES = 25

class CompliBot:
    def __init__(self):
        self.bot = easy.EasyGoPiGo3()
        self.dist_sensor = self.bot.init_distance_sensor()
        self.led = self.bot.init_led('AD1')
        self.cam = cv2.videoCapture()

    def run(self):
        while True:
            while(not self.find_faces()):
                self.avoid_objects()
            self.interaction()

    def find_faces(self):
        pass

    def interaction(self):
        pass

    def avoid_objects(self):
        dist = self.dist_sensor.read_mm()
        if dist <= TURN_DISTANCE:
            self.bot.turn_degrees(TURN_DEGREES)

    def speak(self):
        pass

    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)
