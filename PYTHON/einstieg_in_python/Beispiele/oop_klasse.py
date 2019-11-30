# Definition der Klasse Fahrzeug
class Fahrzeug:
    geschwindigkeit = 0               # Eigenschaft
    def beschleunigen(self, wert):    # Methode
        self.geschwindigkeit += wert
    def ausgabe(self):                # Methode
        print("Geschwindigkeit:", self.geschwindigkeit)

# Objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug()
volvo = Fahrzeug()

# Objektmethoden
volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()
