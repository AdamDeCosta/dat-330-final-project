import easygopigo3 as easy
import cv2 as cv
import numpy as np
import picamera


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

    
    def detectFaces(img_array, cascade):
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) != 0:
            return True
        else:
            return False
            
    def find_faces(self):
        face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 30
            freshest_frame = np.empty((240, 320, 3), dtype = np.uint8)
            camera.capture(freshest_frame, use_video_port = True, format = 'rgb')
            return detectFaces(freshest_frame, face_cascade)

        

    def interaction(self):
        pass

    def avoid_objects(self):
        pass

    def speak(self):
        pass

    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)
