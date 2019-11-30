# Import des Moduls
import fractions

# untersuchte Zahl
x = 1.84953
print("Zahl:", x)

# als Bruch
b3 = fractions.Fraction(x)
print("Fraction:", b3)

# approximiert
b4 = b3.limit_denominator(100)
print("Approximiert auf Nenner max. 100:", b4)

# Genauigkeit
wert = b4.numerator / b4.denominator
print("Wert:", wert)
print("rel. Fehler:", abs((x-wert)/x))
