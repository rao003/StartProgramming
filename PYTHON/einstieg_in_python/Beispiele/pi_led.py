import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)
gp.setup(6, gp.OUT)

gp.output(6, gp.HIGH)
time.sleep(1.5)
gp.output(6, gp.LOW)

gp.cleanup()
