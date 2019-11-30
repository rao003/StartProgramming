# Definition einer Enumeration mit ganzen Zahlen
import enum
class Farbe(enum.IntEnum):
    rot = 5
    gelb = 2
    blau = 4

# Vergleich
x = 2
if x == Farbe.gelb:
    print("Das ist gelb")
print()

# Alle Elemente
for f in Farbe:
    print(f, repr(f))
print()

# Verschiedene Ausgaben und Berechnungen
print(Farbe.gelb)
print(Farbe.gelb * 1)
print(Farbe.gelb * 10)
