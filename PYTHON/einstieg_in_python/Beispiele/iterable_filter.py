# Funktion, die True oder False liefert
def test(a):
    if a>3:
        return True
    else:
        return False

# Funktion mehrmals aufrufen
z = filter(test, [5, 6, -2, 0, 12, 3, -5])

# Ausgabe der Werte, die True ergeben
for element in z:
    print("True:", element)
