import easygopigo3 as easy
import cv2
from subprocess import call
import pandas as pd
from random import seed
from random import randint

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
        data = pd.read_csv('Phrases.csv')

        text = data.sample(1).to_string()

        cmd_beg= 'espeak '
        cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
        cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file

        #Replacing ' ' with '_' to identify words in the text entered
        text = text.replace(' ', '_')

        #Calls the Espeak TTS Engine to read aloud a Text
        call([cmd_beg+cmd_out+text+cmd_end], shell=True)



