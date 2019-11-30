import sys

# Zugriffsversuch
try:
    d = open("obst.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Gezieltes Lesen
for i in range(1,4):
    # Nr Lesen
    d.seek(48*i)
    nr = int(d.read(4))

    # EP Lesen
    d.seek(20 + 48*i)
    ep = float(d.read(8))

    # Ausgabe
    print("Artikel Nr:", nr, ", EP:", ep)

# Schliessen der Datei
d.close()
