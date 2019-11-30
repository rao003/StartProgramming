# Modul copy
import copy

# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):       # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def __str__(self):                 # Ausgabemethode
        return self.bezeichnung + " " \
               + str(self.geschwindigkeit) + " km/h"

# Objekt der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)

# Kopie eines Objektes erzeugen
zweit_opel = Fahrzeug(opel.bezeichnung, opel.geschwindigkeit)
zweit_opel.beschleunigen(30)

# Tiefe Kopie eines Objektes erzeugen
dritt_opel = copy.deepcopy(opel)
dritt_opel.beschleunigen(35)

# Zweite Referenz auf Objekt erzeugen
viert_opel = opel
viert_opel.beschleunigen(20)

# Kontrollausgaben
print("Original:", opel)
print("Kopie:", zweit_opel)
print("Kopie:", dritt_opel)
print("zweite Referenz auf Original:", viert_opel)

# Identisch
print("2:", opel is zweit_opel)
print("3:", opel is dritt_opel)
print("4:", opel is viert_opel)
