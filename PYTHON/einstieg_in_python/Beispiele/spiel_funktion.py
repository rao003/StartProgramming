# Aufgabe
def aufgabe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    erg = a + b
    print("Die Aufgabe:", a, "+", b)
    return erg

# Kommentar
def kommentar(eingabezahl, ergebnis):
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig")
    else:
        print(eingabezahl, "ist falsch")

# Zufallsgenerator
import random
random.seed()

# Aufgabe
c = aufgabe()

# Schleife und Anzahl initialisieren
zahl = c + 1
versuch = 0

# Schleife mit while
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()

    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erfolgreich
        print("Sie haben keine Zahl eingegeben")
        # Schleife unmittelbar fortsetzen
        continue

    # Kommentar
    kommentar(zahl,c)

# Anzahl Versuche
print("Ergebnis: ", c)
print("Anzahl Versuche:", versuch)
