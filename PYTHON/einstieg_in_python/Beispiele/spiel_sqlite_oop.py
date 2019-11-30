import random, time, glob, sqlite3

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
        ausgabe = f"Richtig: {self.richtig:d} von " \
                  f"{self.anzahl:d} in " \
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
    # Highscore in DB speichern
    def speichern(self, name, zeit):
        # Highscore-DB nicht vorhanden, erzeugen
        if not glob.glob("highscore.db"):
            con = sqlite3.connect("highscore.db")
            cursor = con.cursor()
            sql = "CREATE TABLE daten(" \
                  "name TEXT, " \
                  "zeit REAL)"
            cursor.execute(sql)
            con.close()

        # Datensatz in DB schreiben
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "INSERT INTO daten VALUES('" \
              + name + "'," + str(zeit) + ")"
        cursor.execute(sql)
        con.commit()
        con.close()

    # Highscore anzeigen
    def __str__(self):
        # Highscore-DB nicht vorhanden
        if not glob.glob("highscore.db"):
            return "Keine Highscores vorhanden"

        # Highscores laden
        con = sqlite3.connect("highscore.db")
        cursor = con.cursor()
        sql = "SELECT * FROM daten" \
            " ORDER BY zeit LIMIT 10"
        cursor.execute(sql)

        # Ausgabe Highscore
        ausgabe = " P. Name            Zeit\n"
        i = 1
        for dsatz in cursor:
            ausgabe += f"{i:2d}. {dsatz[0]:10}" \
                       f"{dsatz[1]:5.2f} sec\n"
            i = i+1

        # Verbindung beenden
        con.close()
        return ausgabe

# Hauptprogramm
while True:
    # Hauptmenu, Auswahl
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
