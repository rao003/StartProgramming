# True und False
W = True
print("Wahrheitswert:", W)
W = False
print("Wahrheitswert:", W)

W = 5>3
print("5>3:", W)
W = 5<3
print("5<3:", W)
print()

# Datentyp
W = 5>3
print("Typ von 5>3: ", type(W))
print()

# wahre Zahl
Z = 5 + 0.001 - 5
print("Zahl:", Z)
if Z:
    print("Zahl ist", bool(Z))

# nicht wahre Zahl
Z = 5.75 - 5.75
print("Zahl:", Z)
if not Z:
    print("Zahl ist", bool(Z))
print()

# String
S = "Kurt"
print("String:", S)
if S:
    print("String ist nicht leer, also", bool(S))
print()

# Liste
L = [3,4]
print("Liste vorher:", L)
del L[0:2]
print("Liste nachher:", L)
if not L:
    print("Liste ist leer, also", bool(L))
print()

# Tupel
T = (5,8,2)
print("Tupel:", T)
if T:
    print("Tupel ist nicht leer, also", bool(T))
print()

# Dictionary
D = {"Julia":28, "Werner":32}
print("Dictionary vorher:", D)
del D["Julia"]
del D["Werner"]
print("Dictionary nachher:", D)
if not D:
    print("Dictionary ist leer, also", bool(D))
print()

# Set
S = set([5, 7.5, "abc"])
print("Set vorher:", S)
S.clear()
print("Set nachher:", S)
if not S:
    print("Set ist leer, also", bool(S))
print()

