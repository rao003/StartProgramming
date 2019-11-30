# Umrechnungsfaktor
inch = 2.54

# Tabellenkopf
print(f"{'Inch':>7}{'cm':>7}")

# Schleife
for xi in range (15, 41, 5):
    print(f"{xi:7.1f}{xi * inch:7.1f}")
