import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(17, gp.OUT)

gp.output(17, gp.HIGH)
time.sleep(5)
gp.output(17, gp.LOW)

gp.cleanup()


