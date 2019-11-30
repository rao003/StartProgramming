import math

# Funktion, die zwei Werte berechnet
def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius
    return flaeche, umfang

# 1. Aufruf
f, u = kreis(3)
print("Fläche:", f)
print("Umfang:", u)

# 2. Aufruf
x = kreis(3)
print("Fläche:", x[0])
print("Umfang:", x[1])

# Fehler
# a, b, c = kreis(3)
