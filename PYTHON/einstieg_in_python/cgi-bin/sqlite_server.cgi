#!C:\Python38\python.exe
import sqlite3

# Dokument-Typ
print("Content-type: text/html")
print()

# Dokumentbeginn
print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>")
print("<body>")

# Verbindung, Cursor
connection = sqlite3.connect("sqlite/firma.db")
cursor = connection.cursor()

# SQL-Abfrage, Absenden, Ergebnis
sql = "SELECT * FROM personen"
cursor.execute(sql)

# Tabellenausgabe des Ergebnisses
print("<table border='1'>")

# Tabellenkopf
print("<tr><td>Name</td><td>Vorname</td>"
      "<td align='right'>PNr.</td>"
      "<td align='right'>Gehalt</td>"
      "<td>Geburtstag</td></tr>")

# Tabellenzeile
for dsatz in cursor:
    print("<tr>"
        + "<td>" + dsatz[0] + "</td>"
        + "<td>" + dsatz[1] + "</td>"
        + "<td align='right'>" + str(dsatz[2]) + "</td>"
        + f"<td align='right'>{dsatz[3]:.2f}</td>"
        + "<td>" + dsatz[4] + "</td>"
        + "</tr>")

# Tabellenende
print("</table>")

# Verbindung beenden
connection.close()

# Dokumentende
print("</body>")
print("</html>")
