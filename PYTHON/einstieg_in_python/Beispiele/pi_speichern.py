import RPi.GPIO as gp
import os, sys, sqlite3, time

if not os.path.exists("rpi.db"):
    connection = sqlite3.connect("rpi.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE temperatur(zeit REAL, wert REAL)"
    cursor.execute(sql)
    connection.close()
    print("Datenbank erzeugt")
    print()

gp.setmode(gp.BCM)
gp.setwarnings(False)

gp.setup(17, gp.OUT)
gp.setup(6, gp.OUT)
gp.setup(13, gp.OUT)
gp.setup(19, gp.OUT)

dateiName = "/sys/class/thermal/thermal_zone0/temp"

connection = sqlite3.connect("rpi.db")
cursor = connection.cursor()

for i in range(1,5):
    datei = open(dateiName, "r")
    tp = datei.readline()
    datei.close()

    tp = int(tp) / 1000
    print(i, ":", tp, "Grad")

    zeit = time.time()
    sql = "INSERT INTO temperatur VALUES(" + str(zeit) + ", " + str(tp) + ")"
    cursor.execute(sql)
    connection.commit()

    if tp <= 50:
        gp.output(6, gp.HIGH)
        gp.output(19, gp.LOW)
        gp.output(17, gp.LOW)
    else:
        gp.output(6, gp.LOW)
        gp.output(19, gp.HIGH)
        gp.output(17, gp.HIGH)
    time.sleep(1)

sql = "SELECT * FROM temperatur ORDER BY zeit DESC"
cursor.execute(sql)
print()
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

connection.close()
gp.cleanup()
