# Formatierung von Zeichenketten
print("{0:>4}{1:>9}{2:>4}{3:>4}".format
     ("dez", "dual","okt","hex"))

# Formatierung ganzer Zahlen
for z in range(59,69):
    print("{0:4d}{0:9b}{0:4o}{0:4x}".format(z))
print()

# Tabelle mit verschiedenen Objekten
fm = "{0:04d}{1:>12}{2:4d}{3:8.2f} Euro{4:8.2f} Euro"
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}

print("{0:>4}{1:>12}{2:>4}{3:>13}{4:>13}".format
     ("Nr","Name","Anz","EP","GP"))
for x in 23, 8, 42:
    print(fm.format(x, artname[x], anzahl[x],
          epreis[x], anzahl[x] * epreis[x]))

