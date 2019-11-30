import RPi.GPIO as GPIO
import time
import AlphaBot2

Ab = AlphaBot2.AlphaBot2()

Ab.forward()
time.sleep(0.15)
Ab.stop()
time.sleep(1)

Ab.backward()
time.sleep(0.15)
Ab.stop()
time.sleep(1)

Ab.right()
time.sleep(0.2)
Ab.stop()
time.sleep(1)

Ab.left()
time.sleep(0.2)
Ab.stop()
time.sleep(1)

GPIO.cleanup()
