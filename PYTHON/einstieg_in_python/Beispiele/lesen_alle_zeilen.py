import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeilen in eine Liste
allezeilen = d.readlines()

# Schliessen der Datei
d.close()

# Ausgabe und Summierung der Listenelemente
summe = 0
for zeile in allezeilen:
    print(zeile, end="")
    summe += float(zeile)

# Ausgabe der Summe
print("Summe:", summe)


