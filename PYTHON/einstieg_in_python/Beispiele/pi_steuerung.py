import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setwarnings(False)

gp.setup(17, gp.OUT)
gp.setup(6, gp.OUT)
gp.setup(13, gp.OUT)
gp.setup(19, gp.OUT)

dateiName = "/sys/class/thermal/thermal_zone0/temp"

for i in range(1,30):
    datei = open(dateiName, "r")
    tp = datei.readline()
    datei.close()

    tp = int(tp) / 1000
    print(i, ":", tp, "Grad")

    if tp <= 50:
        gp.output(6, gp.HIGH)
        gp.output(19, gp.LOW)
        gp.output(17, gp.LOW)
    else:
        gp.output(6, gp.LOW)
        gp.output(19, gp.HIGH)
        gp.output(17, gp.HIGH)
    time.sleep(1)

gp.cleanup()

