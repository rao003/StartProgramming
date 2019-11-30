import sys, morsen

# Beispieltext codieren
def schreibeCode(text, code):
    for zeichen in text:
        try:
            print(code[zeichen], end=" ")
        except KeyError:
            print(" ", end=" ")
    print()

# Lesefunktion aufrufen
code = morsen.leseCode()

# Schreibfunktion aufrufen
schreibeCode("Hallo Welt", code)

