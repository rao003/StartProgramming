# Ein Objekt, zwei Referenzen
x = 42
y = 42
print("x:", x, "y:", y, "identisch:", x is y)

# Zweites Objekt
y = 56
print("x:", x, "y:", y, "identisch:", x is y)

# Ressourcen sparen
y = 42
print("x:", x, "y:", y, "identisch:", x is y)

# Entfernen, Schritt 1
del y
print("x:", x)

# Entfernen, Schritt 2
del x
try:
    print("x:", x)
except:
    print("Fehler")    
