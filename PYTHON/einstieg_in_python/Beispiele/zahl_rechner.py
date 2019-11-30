import math

a = 4.75
print("Variable a: ", a)
print("Quadratwurzel von a:", math.sqrt(a))
print("Natürlicher Logarithmus von a:", math.log(a))
print("e hoch a:", math.exp(a))
print("10er-Logarithmus von a:", math.log10(a))
print()

b = 34
print("Ganzzahlige Quadratwurzel:", math.isqrt(b))
print()

print("Kreiszahl pi:", math.pi)
print("Eulersche Zahl e:", math.e)
print()

t = 3, 2, -7
print("Produkt:", math.prod(t))
print("Fakultät von 5:", math.factorial(5))
print("Größter gem. Teiler von 60 und 135:", math.gcd(60, 135))
print("Rest:", math.remainder(10.8, 2.5))
print("Rest:", math.remainder(11.8, 2.5))
print()

if math.isclose(3, 2.96, rel_tol=0.01):
    print("Nahe dran")
else:
    print("Nicht nahe dran")
    
if math.isclose(3, 2.97, rel_tol=0.01):
    print("Nahe dran")
else:
    print("Nicht nahe dran")
