# Funktion
def volumen(breite, laenge, tiefe=1, farbe="schwarz"):
    print("Werte:", breite, laenge, tiefe, farbe)
    erg = breite * laenge * tiefe
    print("Volumen:", erg, "Farbe:", farbe)

# Aufrufe
volumen(4, 6, 2, "rot")
volumen(2, 12, 7)
volumen(5, 8)
volumen(4, 7, farbe="rot")
