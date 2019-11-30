# Funktion zur Berechnung einzelner Werte
def quadrat(x):
    return x * x

# Funktion zur Berechnung einzelner Werte
def hochdrei(x):
    return x * x * x

# Funktion zur Ausgabe von Funktionswerten
def ausgabe(unten, oben, schritt, f):
    for x in range(unten, oben, schritt):
        print(x, f(x))
    print()

# Aufruf, Funktionsname ist Parameter
ausgabe(2, 11, 2, quadrat)
ausgabe(1, 6, 1, hochdrei)
