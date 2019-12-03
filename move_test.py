from easygopigo3 import EasyGoPiGo3
from time import time, sleep

SLOW = 50
MED = 200
FAST = 400

# Create an instance of the GoPiGo3 Class
gpg = EasyGoPiGo3

# Drive forward for 5 seconds
gpg.forward()
time.sleep(5)
gpg.stop()

# Drive forward for 12 inches
gpg.drive_inches(12, True)

# Turn left and right
gpg.left()
time.sleep(1)
gpg.right(1)
time.sleep(1)
gpg.stop()

# Speed controls
gpg.set_speed(SLOW)
gpg.drive_inches(12, True)
time.sleep(2)

gpg.set_speed(MED)
gpg.drive_inches(-12, True)
time.sleep(2)

gpg.set_speed(FAST)
gpg.drive_inches(12, True)
gpg.stop()
