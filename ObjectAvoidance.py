import time
import easygopigo3 as easy

TURN_DISTANCE = 20
TURN_DEGREES = 25

gpg = easy.EasyGoPiGo3()
dist_sensor = gpg.init_distance_sensor()

while True:
    print("Distance From Object (mm): " + str(dist_sensor.read_mm()))
    dist = dist_sensor.read_mm()
    if dist <= TURN_DISTANCE:
        gpg.turn_degrees(TURN_DEGREES)
    time.sleep(.1)

