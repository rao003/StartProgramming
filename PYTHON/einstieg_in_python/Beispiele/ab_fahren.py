import RPi.GPIO as GPIO
import time
import AlphaBot2

Ab = AlphaBot2.AlphaBot2()

Ab.forward()
time.sleep(0.15)
Ab.stop()

GPIO.cleanup()
