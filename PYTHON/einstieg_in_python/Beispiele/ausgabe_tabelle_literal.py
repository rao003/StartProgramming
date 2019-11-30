# Formatierung von Zeichenketten
print(f"{'dez':>4}{'dual':>9}{'oct':>4}{'hex':>4}")

# Formatierung ganzer Zahlen
for z in range(59,69):
    print(f"{z:4d}{z:9b}{z:4o}{z:4x}")
print()

# Tabelle mit verschiedenen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}

print(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}")
for x in 23, 8, 42:
    print(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}"
          f"{epreis[x]:8.2f} Euro{anzahl[x] * epreis[x]:8.2f} Euro")

