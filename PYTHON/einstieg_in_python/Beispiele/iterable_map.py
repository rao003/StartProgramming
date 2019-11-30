# Funktion mit einem Parameter
def quad(x):
    erg = x * x
    return erg

# Funktion mit mehr als einem Parameter
def summe(a,b,c):
    erg = a + b + c
    return erg

# Funktion mit einem Parameter mehrmals aufrufen
z = map(quad, [4, 2.5, -1.5])

# Jedes Ergebnis ausgeben
print("Quadrat:")
for element in z:
    print(element)
print()

# Funktion mit mehr als einem Parameter mehrmals aufrufen
z = map(summe, [3, 1.2, 2], [4.8, 2], [5, 0.1, 9])

# Jedes Ergebnis ausgeben
print("Summe:")
for element in z:
    print(element)
