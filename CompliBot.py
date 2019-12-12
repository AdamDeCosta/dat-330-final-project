import easygopigo3 as easy
import cv2

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
        pass

    def speak(self):
        pass



