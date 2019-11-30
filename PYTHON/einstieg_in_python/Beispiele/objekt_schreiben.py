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
    d = open("objekt.bin", "wb")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Eingebautes Objekt
x = ([4,"abc",8], "xyz")
print(x)
pickle.dump(x, d)

# Objekt der eigenen Klasse
opel = Fahrzeug("Opel Admiral", 40)
print(opel)
pickle.dump(opel, d)

# Variable Anzahl an Objekten
pickle.dump(3, d)
pickle.dump("Berlin", d)
pickle.dump("Hamburg", d)
pickle.dump("Dortmund", d)

# Datei schliessen
d.close()
