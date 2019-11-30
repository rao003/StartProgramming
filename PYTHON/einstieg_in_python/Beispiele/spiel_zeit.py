# Module
import random, time

# Initialisierung
random.seed()
richtig = 0
startzeit = time.time()

# 5 Aufgaben
for aufgabe in range(5):
    # Aufgabe mit Ergebnis
    a = random.randint(10,30)
    b = random.randint(10,30)
    c = a + b
    print("Aufgabe", aufgabe+1, "von 5:", a, "+", b)

    # Eingabe
    try:
        zahl = int(input("Bitte eine Zahl eingeben: "))
        if zahl == c:
            print("Richtig")
            richtig += 1
        else:
            raise
    except:
        print("Falsch")

# Auswertung
endzeit = time.time()
differenz = endzeit - startzeit
print(f"Richtig: {richtig:d} von 5 in {differenz:.2f} Sekunden")
print("Ergebnis erzielt:", time.strftime("%d.%m.%Y %H:%M:%S"))
