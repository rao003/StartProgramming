# Zahl mit Nachkommastellen
x = 100/7
y = 2/7
print("Zahlen:", x, y)
print()

# Format f
print("Format f, Standard:   {0:f} {0:f} {1:f}".format(x,y))
print("Format f, nach Komma: {0:.25f}".format(x))
print("Format f, gesamt:     {0:15.10f}".format(x))
print()

# Format e
print("Format e, Standard:   {0:e}".format(x))
print("Format e, nach Komma: {0:.3e}".format(x))
print("Format e, gesamt:     {0:12.3e}".format(x))
print()

# Format %
print("Format %, Standard:   {0:%}".format(y))
print("Format %, nach Komma: {0:.3%}".format(y))
print("Format %, gesamt:     {0:12.3%}".format(y))
