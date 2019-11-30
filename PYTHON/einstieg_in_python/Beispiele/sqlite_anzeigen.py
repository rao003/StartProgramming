import sqlite3

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL-Abfrage
sql = "SELECT * FROM personen"

# Kontrollausgabe der SQL-Abfrage
# print(sql)

# Absenden der SQL-Abfrage
# Empfang des Ergebnisses
cursor.execute(sql)

# Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4])

# Verbindung beenden
connection.close()

