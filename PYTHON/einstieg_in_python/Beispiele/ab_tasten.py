import sys
import termios
import tty

import RPi.GPIO as GPIO
import time
import AlphaBot2
Ab = AlphaBot2.AlphaBot2()

fd = sys.stdin.fileno()
attr = termios.tcgetattr(fd)
tty.setraw(fd)

while True:
    key = sys.stdin.read(1)

    if key == 'w':
        Ab.forward()
        time.sleep(0.2)
        Ab.stop()
    elif key == 's':
        Ab.backward()
        time.sleep(0.2)
        Ab.stop()
    elif key == 'a':
        Ab.left()
        time.sleep(0.2)
        Ab.stop()
    elif key == 'd':
        Ab.right()
        time.sleep(0.2)
        Ab.stop()
    elif key == 'q':
        GPIO.cleanup()
        break

termios.tcsetattr(fd, termios.TCSADRAIN, attr)
GPIO.cleanup()
