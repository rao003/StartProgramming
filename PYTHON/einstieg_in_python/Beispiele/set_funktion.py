# Set
s1 = set([8, 15, "x"])
print("Original:", s1)

# Kopie
s2 = s1.copy()
print("Kopie:", s2)

# Element hinzu
s1.add("abc")
print("Element hinzu:", s1)

# Element entnehmen
s1.discard("x")
print("Element entnommen:", s1)

# Leeren
s1.clear()
print("geleert:", s1)
