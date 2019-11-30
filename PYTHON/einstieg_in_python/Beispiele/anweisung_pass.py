# Funktions-Dummy
def QuadraturDesKreises():
    pass

# Funktionsaufruf
QuadraturDesKreises()

# Nur else-Zweig interessant
a = -12
b = 6
c = 6.2

if a >= 0 and b >= 0 and c >= 0:
    pass
else:
    print("Eine der Zahlen ist negativ")

# Ein Zweig nicht interessant
if a == 1:
    print("Fall 1")
elif a == 2:
    print("Fall 2")
elif a < 0:
    pass
else:
    print("Ansonsten")
