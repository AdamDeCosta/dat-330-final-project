import easygopigo3 as easy
import cv2
from subprocess import call
import pandas as pd
from random import seed
from random import randint
import time

TURN_DISTANCE = 20
TURN_DEGREES = 25

# Speed Variables for clarity in code
SLOW = 50
MED = 200
FAST = 400

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

    def find_faces(self):
        pass

    def interaction(self):
        pass

    def default_move(self, distance):
        self.bot.speed(SLOW)
        self.bot.drive_inches(distance, True)

    def end_interaction_move(self):
        self.bot.speed(MED)
        self.bot.turn_degrees(180)
        self.bot.forward(10)

    def avoid_objects(self):
        dist = self.dist_sensor.read_mm()
        while dist <= TURN_DISTANCE:
            self.bot.turn_degrees(TURN_DEGREES)
            dist = self.dist_sensor.read_mm()
            self.default_move(24)   # Change the distance here as needed

    def speak(self):


        text = self.phrases.sample(1).to_string()

        cmd_beg= 'espeak '
        cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To 
play back the stored .wav file and to dump the std errors to /dev/null
        cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the 
voice file

        #Replacing ' ' with '_' to identify words in the text entered
        text = text.replace(' ', '_')

        #Calls the Espeak TTS Engine to read aloud a Text
        call([cmd_beg+cmd_out+text+cmd_end], shell=True)


    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)

