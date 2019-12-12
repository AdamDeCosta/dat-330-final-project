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
         with open('Phrases.csv', 'r') as f: #get the phrase from the file
            reader = csv.reader(f)
            phrases = list(reader)

        new_list = []
        for j in phrases:
            for i in j:
                new_list.append(i)
        del phrases #Memory Control
        phrase = "Hello There, " + random.choice(new_list) #get a Random Phrase
        print(phrase)

    def avoid_objects(self):
        pass

    def speak(self):
        pass

    def light_on(self):
        self.led.light_max(100)

    def light_off(self):
        self.led.light_max(0)
