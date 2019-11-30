# Umrechnungsfaktor
inch = 2.54

# Erste Eingabe
print("Bitte geben Sie den inch-Wert ein:")
xi = float(input())

# while-Schleife
while xi != 0:
    # Umrechnung, Ausgabe
    xcm = xi * inch
    print(xi, "inch sind", xcm, "cm")

    # Weitere Eingabe
    print("Bitte geben Sie den inch-Wert ein:")
    xi = float(input())

