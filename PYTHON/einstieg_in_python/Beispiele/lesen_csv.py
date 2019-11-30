import sys

# Zugriffsversuch
try:
    d = open("daten.csv")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des gesamten Texts
gesamtertext = d.read()

# Schliessen der Datei
d.close()

# Umwandeln in eine Liste von Zeilen
zeilenliste = gesamtertext.split(chr(10))

# Jede Zeile umwandeln in Liste von int, string, float
li = []
for zeile in zeilenliste:
    if zeile:
        zwliste = zeile.split(";")
        li.append([int(zwliste[0]),
            zwliste[1],
            float(zwliste[2].replace(",", "."))])

# Ausgabe
for p in li:
    print(f"{p[0]:d} {p[1]} {p[2]:.2f}")
