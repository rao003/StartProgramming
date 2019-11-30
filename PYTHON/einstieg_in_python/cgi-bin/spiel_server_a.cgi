#!C:\Python38\python.exe

# Module
import cgi, cgitb, sys, random, time

# Ausgabe bei Fehler
cgitb.enable()

# Initialisierung Zufallsgenerator
random.seed()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# Header
print("Content-type: text/html")
print()

# HTML-Dokumentbeginn
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")
print("<p><b>Kopfrechnen</b></p>")

# Falls kein Name eingetragen
if not "spielername" in form:
        print("<p>Kein Name, kein Spiel</p>")
        print("<a href='http://localhost/Python38/"
              "spiel_server.htm'>Zur&uuml;ck</a>")
        print("</body>")
        print("</html>")
        sys.exit(0)

# Formularbeginn
print("<form action='spiel_server_b.cgi'>")

# Spielername
print("<p>Hallo <b>", form["spielername"].value,
      "</b>, Ihre Aufgaben</p>")
print("<input name='spielername' type='hidden' "
      "value='" + form["spielername"].value + "'>")

# Startzeit
startzeit = time.time()
print("<input name='startzeit' type='hidden' "
      "value='" + str(startzeit) + "'>")

# Tabellenbeginn
print("<table border='0'>")

# 5 Aufgaben
for aufgabe in range(5):
        # Aufgabe mit Ergebnis
        a = random.randint(10,30)
        b = random.randint(10,30)
        c = a + b

        # Tabellenzeile
        print("<tr>")
        print("<td>&nbsp;" + str(aufgabe+1)
              + ".&nbsp;</td>")
        print("<td>&nbsp;" + str(a) + "&nbsp;</td>")
        print("<td>&nbsp;+&nbsp;</td>")
        print("<td>&nbsp;" + str(b) + "&nbsp;</td>")
        print("<td>&nbsp;=&nbsp;</td>")
        print("<td><input name='ein" + str(aufgabe)
              + "' size='12'></td>")
        print("</tr>")

        # Richtiges Ergebnis senden
        print("<input name='erg" + str(aufgabe) + "'"
              + "type='hidden' value='" + str(c) + "'>")

# Tabellenende
print("</table>")

# Absenden
print("<p><input type='submit' value='Fertig'></p>")

# HTML-Dokumentende
print("</form>")
print("</body>")
print("</html>")
