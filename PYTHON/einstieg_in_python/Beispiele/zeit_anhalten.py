# Modul time
import time

# Start
startzeit = time.time()
print("Start:", startzeit)

# Zeitangaben, jeweils mit Pause
for i in range(5):
    time.sleep(2)
    print(time.time())

# Ende
endzeit = time.time()
print("Ende:", endzeit)

# Abstand
differenz = endzeit - startzeit
print("Differenz:", differenz)
