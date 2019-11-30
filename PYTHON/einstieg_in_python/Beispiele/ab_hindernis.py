import RPi.GPIO as GPIO
import time
import AlphaBot2

Ab = AlphaBot2.AlphaBot2()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(19) == 0:
            Ab.stop()
            time.sleep(0.5)
            Ab.backward()
            time.sleep(0.5)
            Ab.left()
            time.sleep(0.5)
            Ab.stop()
        elif GPIO.input(16) == 0:
            Ab.stop()
            time.sleep(0.5)
            Ab.backward()
            time.sleep(0.5)
            Ab.right()
            time.sleep(0.5)
            Ab.stop()
        else:
            Ab.forward()
except KeyboardInterrupt:
    GPIO.cleanup()

