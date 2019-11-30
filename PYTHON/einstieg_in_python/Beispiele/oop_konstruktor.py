# Definition der Klasse Fahrzeug
class Fahrzeug:
    # Konstruktormethode
    def __init__(self, bez="(leer)", ge=0):
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    # Destruktormethode
    def __del__(self):
        print("Objekt", self.bezeichnung, "entfernt")

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
        self.ausgabe()
    def ausgabe(self):
        print(self.bezeichnung, self.geschwindigkeit, "km/h")

# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)
ford = Fahrzeug("Ford Mondeo")
mercedes = Fahrzeug(ge=60)

# Objekte betrachten
opel.ausgabe()
volvo.ausgabe()
ford.ausgabe()
mercedes.ausgabe()

# Objektmethode
volvo.beschleunigen(20)

# Destruktor aufrufen
del opel
del volvo

# Aufruf nicht mehr gestattet
# opel.ausgabe()
