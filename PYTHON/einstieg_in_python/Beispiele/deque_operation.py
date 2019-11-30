# Modul
import collections

# Neu erzeugen
d = collections.deque([8, 18, 28])
print("Neu erzeugt:", d)

# Kopie
dk = d.copy()
print("Kopie:", dk)

# Alle Elemente einzeln
print("Alle Elemente einzeln: ", end="")
for x in d:
    print(x, end=" ")
print()

# Einzelne Elemente
try:
    print("Zweites Element von links:", d[1])
except:
    print("Dieser Index existiert nicht")

try:
    print("Erstes Element von rechts:", d[-1])
except:
    print("Dieser Index existiert nicht")

# Multiplizieren
d = d * 2
print("Mit 2 multipliziert:", d)

# Addieren
dzwei = collections.deque([9, 19, 29])
d = d + dzwei
print("Zweite deque addiert:", d)

# Deque leeren
d.clear()
print("Nach Leerung:", d)
