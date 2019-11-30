# Funktion
def quotient(a, b):
    try:
        c = a/b
        return c
    except:
        print("Funktion meldet Fehler")

# liefert Ergebnis
erg = quotient(7,4)
if erg:
    print("Ergebnis:", erg)
print()

# liefert Fehler
erg = quotient(7,0)
if not erg:
    print("Programm meldet Fehler")
print("Ergebnis:", erg)
print("Typ des Ergebnisses:", type(erg))
print()

# Konstante None
Z = None
print("Z:", Z)
if Z is None:
    print("Objekt ist das Nichts, also", bool(Z))

