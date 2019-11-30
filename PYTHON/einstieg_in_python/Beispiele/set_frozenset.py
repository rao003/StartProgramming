# Set
s = set([8, 15, "x", 8])
print("Set:", s)

# Frozenset
fs = frozenset([8, 15, "x", 8])
print("Frozenset:", fs)
for x in fs:
    print(x)
try:
    fs.discard("x")
except:
    print("Fehler")
