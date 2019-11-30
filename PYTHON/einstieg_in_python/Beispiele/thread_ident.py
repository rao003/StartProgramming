# Module
import time, threading

# Thread-Funktion
def show():
    id = threading.get_ident()
    print("Start Thread", id)
    for i in range(5):
        print(i, "Thread", id)
        time.sleep(1.5)
    print("Ende Thread", id)
    return

# Hauptprogramm
id = threading.get_ident()
print("Start Hauptprogramm", id)

t1 = threading.Thread(target=show)
t1.start()
time.sleep(0.5)
t2 = threading.Thread(target=show)
t2.start()

time.sleep(10)
print("Ende Hauptprogramm", id)
