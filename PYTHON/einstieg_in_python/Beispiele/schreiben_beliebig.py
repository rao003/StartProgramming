import sys

# Zugriffsversuch
try:
    d = open("obst.txt", "r+")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des Einzelpreises
d.seek(68)
ep_str = d.read(8)
ep = float(ep_str)

# Schreiben des Einzelpreises
d.seek(68)
ep = ep + 0.2
d.write(f"{ep:8.2f}")

# Lesen des Gesamtpreises
d.seek(81)
gp_str = d.read(8)
gp = float(gp_str)

# Schreiben des Gesamtpreises
d.seek(81)
gp = gp + 0.2
d.write(f"{gp:8.2f}")

# Schliessen der Datei
d.close()
