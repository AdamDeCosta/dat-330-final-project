import easygopigo3 as easy
import cv2 as cv
import numpy as np
import picamera
from subprocess import call
import pandas as pd
from random import seed
from random import randint
import time

TURN_DISTANCE = 20
TURN_DEGREES = 25

class CompliBot:
    def __init__(self):
        self.bot = easy.EasyGoPiGo3()
        self.dist_sensor = self.bot.init_distance_sensor()
        self.led = self.bot.init_led('AD1')
        self.cam = cv2.videoCapture()
        self.phrases = pd.read_csv('Phrases.csv')

    def run(self):
        while True:
            while(not self.find_faces()):
                self.avoid_objects()
            self.interaction()

    
    def detectFaces(img_array, cascade):
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) != 0:
            return True
        else:
            return False
            
    def find_faces(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        with picamera.PiCamera() as camera:
            camera.resolution = (320, 240)
            camera.framerate = 30
            freshest_frame = np.empty((240, 320, 3), dtype = np.uint8)
            camera.capture(freshest_frame, use_video_port = True, format = 'rgb')
            return detectFaces(freshest_frame, face_cascade)

        

    def interaction(self):
        pass

    def avoid_objects(self):
        dist = self.dist_sensor.read_mm()
        if dist <= TURN_DISTANCE:
            self.bot.turn_degrees(TURN_DEGREES)

    def speak(self):


        text = self.phrases.sample(1).to_string()

        cmd_beg= 'espeak '
        cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
        cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file

        #Replacing ' ' with '_' to identify words in the text entered
        text = text.replace(' ', '_')

        #Calls the Espeak TTS Engine to read aloud a Text
        call([cmd_beg+cmd_out+text+cmd_end], shell=True)


    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)
