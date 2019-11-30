# Eingabe
print("Geben Sie Ihr Gehalt in Euro ein:")
gehalt = float(input())
print("Geben Sie Ihren Familienstand ein"
      + " (1=ledig, 2=verheiratet):")
familienstand = int(input())

# Umrechnung
if gehalt > 4000 and familienstand == 1:
    steuerbetrag = gehalt * 0.26
elif gehalt <= 4000 and familienstand == 2:
    steuerbetrag = gehalt * 0.18
else:
    steuerbetrag = gehalt * 0.22

# Ausgabe
print("Es ergibt sich eine Steuer von", steuerbetrag, "Euro")
