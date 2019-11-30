import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen und Ausgabe einzelner Zeilen
zeile1 = d.readline()
print(zeile1, end="")
zeile2 = d.readline()
print(zeile2, end="")

# Summierung und Ausgabe
summe = float(zeile1) + float(zeile2)
print("Summe:", summe)

# Schliessen der Datei
d.close()

