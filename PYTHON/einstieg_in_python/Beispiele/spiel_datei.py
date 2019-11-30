# Module
import random, time, glob, pickle

######################################################

# Funktion Highscore Lesen
def hs_lesen():
    # Liste wird hier erzeugt
    global hs_liste

    # Kein Highscore vorhanden, leere Liste
    if not glob.glob("highscore.bin"):
        hs_liste = []
        return

    # Highscore vorhanden, laden
    d = open("highscore.bin", "rb")
    hs_liste = pickle.load(d)
    d.close()

######################################################

# Funktion Highscore Anzeigen
def hs_anzeigen():
    # Highscore nicht vorhanden
    if not hs_liste:
        print("Keine Highscores vorhanden")
        return

    # Ausgabe Highscore
    print(" P. Name            Zeit")
    for i in range(len(hs_liste)):
        print(f"{i+1:2d}. {hs_liste[i][0]:10}"
              f" {hs_liste[i][1]:5.2f} sec")
        if i >= 9:
            break

######################################################

# Funktion Highscore Schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin","wb")
    pickle.dump(hs_liste,d)
    d.close()

######################################################

# Funktion Spiel
def spiel():
    # Eingabe des Namens
    name = input("Bitte geben Sie Ihren "
                 "Namen ein (max. 10 Zeichen): ")
    name = name[0:10]

    # Initialisierung Counter und Zeit
    richtig = 0
    startzeit = time.time()

    # 5 Aufgaben
    for aufgabe in range(5):
        # Aufgabe mit Ergebnis
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        # Eingabe
        try:
            zahl = int(input("Aufgabe "
                + str(aufgabe+1) + " von 5: "
                + str(a) + " + " + str(b) + " : "))
            if zahl == c:
                print("*** Richtig ***")
                richtig += 1
            else:
                raise
        except:
            print("* Falsch *")

    # Auswertung
    endzeit = time.time()
    differenz = endzeit - startzeit
    print(f"Ergebnis: {richtig:d} von 5 in "
          f"{differenz:.2f} Sekunden", end = "")
    if richtig == 5:
        print(", Highscore")
    else:
        print(", leider kein Highscore")
        return

    # Mitten in Liste schreiben
    gefunden = False
    for i in range(len(hs_liste)):
        # Einsetzen in Liste
        if differenz < hs_liste[i][1]:
            hs_liste.insert(i, [name, differenz])
            gefunden = True
            break

    # Ans Ende der Liste schreiben
    if not gefunden:
        hs_liste.append([name, differenz])

    # Highscoreliste anzeigen
    hs_anzeigen()

######################################################

# Hauptprogramm

# Initialisierung Zufallsgenerator
random.seed()

# Highscore aus Datei in Liste lesen
hs_lesen()

# Endlosschleife
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("Bitte eingeben "
            "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    # Aufruf einer Funktion oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs_anzeigen()
    elif menu == 2:
        spiel()
    else:
        print("Falsche Eingabe")

# Highscore aus Liste in Datei schreiben
hs_schreiben()
