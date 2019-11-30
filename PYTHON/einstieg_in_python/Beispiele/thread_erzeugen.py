# Module
import time, threading

# Thread-Funktion
def show():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Thread")

# Hauptprogramm
print("Start Hauptprogramm")
t = threading.Thread(target=show)
t.start()
time.sleep(10)
print("Ende Hauptprogramm")
