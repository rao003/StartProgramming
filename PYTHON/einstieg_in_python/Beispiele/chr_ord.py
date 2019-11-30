# Ziffern
for i in range(48,58):
    print(chr(i), end="")
print()

# große Buchstaben
for i in range(65,91):
    print(chr(i), end="")
print()

# kleine Buchstaben
for i in range(97,123):
    print(chr(i), end="")
print()

# Codenummern
for z in "Robinson":
    print(ord(z), end=" ")
print()

# Verschoben
for z in "Robinson":
    print(chr(ord(z)+1), end="")
