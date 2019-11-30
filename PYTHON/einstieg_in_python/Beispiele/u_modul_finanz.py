# Funktion
def steuer(gehalt):
    # Umrechnung
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18

    # Ergebnis senden
    return steuerbetrag
