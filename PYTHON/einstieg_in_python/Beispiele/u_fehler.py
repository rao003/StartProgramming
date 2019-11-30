# Umrechnungsfaktor
inch = 2.54

# Initialisierung der while-Schleife
fehler = 1

# Schleife bei falscher Eingabe
while fehler == 1:
    # Eingabe
    print("Bitte geben Sie den inch-Wert ein")
    xi = input()

    # Versuch der Umwandlung
    try:
        xi = float(xi)
        fehler = 0
    # Fehler bei Umwandlung
    except:
        print("Falsche Eingabe")

# Umrechnung, Ausgabe
xcm = xi * inch
print(xi, "inch sind", xcm, "cm")



