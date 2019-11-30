# Modul
import re

# 1: Exakter Text
tx = "Haus und Maus und Laus"
print(tx)
erg = re.findall("Maus",tx)
print("1: ", erg)

# 2: Wahl zwischen bestimmten Zeichen
erg = re.findall("[HM]aus",tx)
print("2: ", erg)

# 3: Alle Buchstaben aus Bereich
erg = re.findall("[L-M]aus",tx)
print("3: ", erg)

# 4: Alle Buchstaben nicht aus Bereich
erg = re.findall("[^L-M]aus",tx)
print("4: ", erg)

# 5: Beliebiges Zeichen
erg = re.findall(".aus",tx)
print("5: ", erg)

# 6: Suchbegriff nur am Anfang des Textes
erg = re.findall("^.aus",tx)
print("6: ", erg)

# 7: Suchbegriff nur am Ende des Textes
erg = re.findall(".aus$",tx)
print("7: ", erg)
print()

# 8: alle Ziffern aus Bereich
tx = "0172-445633"
print(tx)
erg = re.findall("[0-2]",tx)
print("8: ", erg)

# 9: alle Zeichen nicht aus Ziffernbereich
erg = re.findall("[^0-2]",tx)
print("9: ", erg)

# 10: alle Zeichen oder Ziffern, die angegeben sind
erg = re.findall("[047-]",tx)
print("10: ", erg)
print()

# 11: Wiederholung, beliebig oft
tx = "aa und aba und abba und abbba und aca"
print(tx)
erg = re.findall("ab*a",tx)
print("11: ", erg)

# 12: Wiederholung, 1 oder mehr
erg = re.findall("ab+a",tx)
print("12: ", erg)

# 13: Wiederholung, 0 oder 1
erg = re.findall("ab?a",tx)
print("13: ", erg)

# 14: Wiederholung, m bis n
erg = re.findall("ab{2,3}a",tx)
print("14: ", erg)

# 15: Wiederholung der max. Menge von Zeichen
tx = "aa und aba und abba und aca und addda"
erg = re.findall("a.*a",tx)
print("15: ", erg)

# 16: Wiederholung der min. Menge von Zeichen
erg = re.findall("a.*?a",tx)
print("16: ", erg)
