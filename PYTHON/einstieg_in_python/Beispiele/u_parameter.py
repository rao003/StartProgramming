# Funktion
def steuer(gehalt):
    # Umrechnung
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18

    # Ausgabe
    print("Gehalt:", gehalt, "Euro, Steuer:",
          steuerbetrag, "Euro")
    
# Verschiedene Werte
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)
