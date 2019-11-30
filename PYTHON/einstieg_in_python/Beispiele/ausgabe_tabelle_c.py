# Formatierung von Zeichenketten
print("%4s%4s%4s" % ("dez", "okt","hex"))

# Formatierung ganzer Zahlen
for z in range(59,69):
    print("%4d%4o%4x" % (z, z, z))
print()

# Tabelle mit verschiedenen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}

print("%4s%12s%4s%13s%13s" % ("Nr","Name","Anz","EP","GP"))
for x in 23, 8, 42:
    print("%04d%12s%4d%8.2f Euro%8.2f Euro" % (x, artname[x],
        anzahl[x], epreis[x], anzahl[x] * epreis[x]))

