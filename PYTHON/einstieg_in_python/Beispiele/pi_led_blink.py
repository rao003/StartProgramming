import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(6, gp.OUT)

for i in range(5):
    gp.output(6, gp.HIGH)
    time.sleep(0.5)
    gp.output(6, gp.LOW)
    time.sleep(0.5)

gp.cleanup()
