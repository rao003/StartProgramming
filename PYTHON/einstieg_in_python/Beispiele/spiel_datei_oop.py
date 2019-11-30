import random, time, glob

# Klasse "Spiel"
class Spiel:
    def __init__(self):
        # Start des Spiels
        random.seed()
        self.richtig = 0
        self.anzahl = 5
        s = input("Bitte geben Sie Ihren "
            "Namen ein (max. 10 Zeichen): ")
        self.spieler = s[0:10]

    def spielen(self):
        # Spielablauf
        for i in range(1,self.anzahl+1):
            a = Aufgabe(i, self.anzahl)
            print(a)
            self.richtig += a.beantworten()

    def messen(self, start):
        # Zeitmessung
        if start:
            self.startzeit = time.time()
        else:
            endzeit = time.time()
            self.zeit = endzeit - self.startzeit

    def __str__(self):
        # Ergebnis
        ausgabe = f"Richtig: {self.richtig:d} von" \
                  f" {self.anzahl:d} in " \
                  f"{self.zeit:.2f} Sekunden"
        if self.richtig == self.anzahl:
            ausgabe += ", Highscore"
            hs = Highscore()
            hs.speichern(self.spieler, self.zeit)
            print(hs)
        else:
            ausgabe += ", leider kein Highscore"
        return ausgabe

# Klasse "Aufgabe"
class Aufgabe:
    # Aufgabe initialisieren
    def __init__(self, i, anzahl):
        self.nr = i
        self.gesamt = anzahl

    # Aufgabe stellen
    def __str__(self):
        a = random.randint(10,30)
        b = random.randint(10,30)
        self.ergebnis = a + b
        return "Aufgabe " + str(self.nr) \
            + " von " + str(self.gesamt) + " : " \
            + str(a) + " + " + str(b)
        
    # Aufgabe beantworten
    def beantworten(self):
        try:
            if self.ergebnis == int(input()):
                print(self.nr, ": ***Richtig ***")
                return 1
            else:
                raise
        except:
            print(self.nr, ": *** Falsch ***")
            return 0

# Klasse "Highscore"
class Highscore:
    # Liste aus Datei lesen
    def __init__(self):
        self.liste = []
        if not glob.glob("highscore.csv"):
            return
        d = open("highscore.csv")
        zeile = d.readline()
        while zeile:
            teil = zeile.split(";")
            name = teil[0]
            zeit = teil[1][0:len(teil[1])-1]
            zeit = zeit.replace(",", ".")
            self.liste.append([name, float(zeit)])
            zeile = d.readline()
        d.close()

    # Liste ändern
    def aendern(self, name, zeit):
        # Mitten in Liste schreiben
        gefunden = False
        for i in range(len(self.liste)):
            # Einsetzen in Liste
            if zeit < self.liste[i][1]:
                self.liste.insert(i, [name, zeit])
                gefunden = True
                break

        # Ans Ende der Liste schreiben
        if not gefunden:
            self.liste.append([name, zeit])

    # Liste ändern, in Datei speichern
    def speichern(self, name, zeit):
        self.aendern(name, zeit)
        d = open("highscore.csv", "w")
        for element in self.liste:
            name = element[0]
            zeit = str(element[1]).replace(".", ",")
            d.write(name + ";" + zeit + "\n")
        d.close()

    # Liste anzeigen
    def __str__(self):
        # Highscore nicht vorhanden
        if not self.liste:
            return "Keine Highscores vorhanden"

        # Ausgabe Highscore
        ausgabe = " P. Name            Zeit\n"
        for i in range(len(self.liste)):
            ausgabe += f"{i+1:2d}. {self.liste[i][0]:10}" \
                       f"{self.liste[i][1]:5.2f} sec\n"
            if i >= 9:
                break
        return ausgabe

# Hauptprogramm
while True:
    # Hauptmenü, Auswahl
    try:
        menu = int(input("Bitte eingeben "
            "(0: Ende, 1: Highscores, 2: Spielen): "))
    except:
        print("Falsche Eingabe")
        continue

    # Anlegen eines Objekts oder Ende
    if menu == 0:
        break
    elif menu == 1:
        hs = Highscore()
        print(hs)
    elif menu == 2:
        s = Spiel()
        s.messen(True)
        s.spielen()
        s.messen(False)
        print(s)
    else:
        print("Falsche Eingabe")
