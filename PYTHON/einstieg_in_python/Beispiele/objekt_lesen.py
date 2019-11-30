import pickle, sys

# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):
        return self.bezeichnung + " " \
           + str(self.geschwindigkeit) + " km/h"

# Zugriffsversuch
try:
    d = open("objekt.bin", "rb")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Eingebautes Objekt
x = pickle.load(d)
print(x)

# Objekt der eigenen Klasse
opel = pickle.load(d)
print(opel)

# Variable Anzahl an Objekten
anzahl = pickle.load(d)
for i in range(anzahl):
    print(pickle.load(d))

# Datei schliessen
d.close()
