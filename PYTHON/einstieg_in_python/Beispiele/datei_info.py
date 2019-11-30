import os, time

# Informationstupel
tu = os.stat("obst.txt")

# Elemente des Tupels
groesse = tu[6]
print("Byte:", groesse)

zugr = time.localtime(tu[7])
print("Letzter Zugriff:",
      time.strftime("%d.%m.%Y %H:%M:%S", zugr))

mod = time.localtime(tu[8])
print("Letzte Modifikation:",
      time.strftime("%d.%m.%Y %H:%M:%S", mod))

