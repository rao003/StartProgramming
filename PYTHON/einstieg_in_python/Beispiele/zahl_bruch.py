# Import des Moduls
import fractions

# Bruch
z = 12
n = 28
print("Bruch:", z, "/", n)

# als Fraction
b1 = fractions.Fraction(z, n)
print("Fraction:", b1)
print("Z, N:", b1.numerator, b1.denominator)
wert = b1.numerator / b1.denominator
print("Wert:", wert)
print()

# Umrechnen
x = 2.375
print("Zahl:", x)
b2 = fractions.Fraction(x)
print("Fraction:", b2)
