# Eingabe
print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())

# Umrechnung
if gehalt > 2500:
    steuerbetrag = gehalt * 0.22
else:
    steuerbetrag = gehalt * 0.18

# Ausgabe
print("Es ergibt sich eine Steuer von",
      steuerbetrag, "Euro")
