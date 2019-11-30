#!C:\Python38\python.exe

# Module
import cgi, cgitb, time, glob, pickle

# Ausgabe bei Fehler
cgitb.enable()

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
    # Ausgabe Highscore
    print("<table>")
    print("<tr><td>Platz</td><td>&nbsp;Name&nbsp;</td>"
          "<td align='right'>Zeit</td></tr>")
    for i in range(len(hs_liste)):
        print("<tr>")
        print("<td align='right'>" + str(i+1) + "</td>")
        print("<td>&nbsp;" + hs_liste[i][0]
              + "&nbsp;</td>")
        print(f"<td align='right'>{hs_liste[i][1]:.2f} sec</td>")
        print("</tr>")

        if i >= 9:
            break
    print("</table>")

######################################################

# Funktion Highscore Schreiben
def hs_schreiben():
    # Zugriff
    d = open("highscore.bin","wb")
    pickle.dump(hs_liste,d)
    d.close()

######################################################

# Funktion Highscore Hinzu
def hs_hinzu(name, differenz):
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

######################################################

# Hauptprogramm

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# Zeit berechnen
endzeit = time.time()
differenz = endzeit - float(form["startzeit"].value)

# Header
print("Content-type: text/html")
print()

# HTML-Dokumentbeginn
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")
print("<p><b>Kopfrechnen</b></p>")

# Spielername
print("<p>Hallo <b>", form["spielername"].value,
      "</b>, Ihr Ergebnis</p>")

# Auswertung
richtig = 0
for aufgabe in range(5):
    if "ein" + str(aufgabe) in form:
        if form["ein" + str(aufgabe)].value == \
                form["erg" + str(aufgabe)].value:
            richtig += 1

# Ausgabe
print(f"<p>{richtig:d} von 5 in " \
      f"{differenz:.2f} Sekunden", end = "")

# Highscore
if richtig == 5:
    print(", Highscore</p>")
    hs_lesen()
    hs_hinzu(form["spielername"].value, differenz)
    hs_schreiben()
    hs_anzeigen()
else:
    print(", leider kein Highscore</p>")

# Hyperlink zum Anfang
print("<p><a href='http://localhost/Python38/"
      "spiel_server.htm'>Zum Start</a></p>")

# HTML-Dokumentende
print("</body>")
print("</html>")
