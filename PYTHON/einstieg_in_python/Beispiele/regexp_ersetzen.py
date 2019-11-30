# Modul
import re

# 1: Exakter Text
tx = "Haus und Maus und Laus"
print(tx)
txneu = re.sub("Maus","x",tx)
print("1: ", txneu)

# 2: Wahl zwischen bestimmten Zeichen
txneu = re.sub("[H|M]aus","x",tx)
print("2: ", txneu)

# 3: alle Buchstaben aus Bereich
txneu = re.sub("[L-M]aus","x",tx)
print("3: ", txneu)

# 4: alle Buchstaben nicht aus Bereich
txneu = re.sub("[^L-M]aus","x",tx)
print("4: ", txneu)

# 5: Beliebiges Zeichen
txneu = re.sub(".aus","x",tx)
print("5: ", txneu)

# 6: Suchbegriff nur am Anfang des Textes
txneu = re.sub("^.aus","x",tx)
print("6: ", txneu)

# 7: Suchbegriff nur am Ende des Textes
txneu = re.sub(".aus$","x",tx)
print("7: ", txneu)
print()

# 8: alle Ziffern aus Bereich
tx = "0172-445633"
print(tx)
txneu = re.sub("[0-2]","x",tx)
print("8: ", txneu)

# 9: alle Zeichen nicht aus Ziffernbereich
txneu = re.sub("[^0-2]","x",tx)
print("9: ", txneu)

# 10: alle Zeichen oder Ziffern, die angegeben sind
txneu = re.sub("[047-]","x",tx)
print("10: ", txneu)
print()

# 11: Wiederholung, beliebig oft
tx = "aa und aba und abba und abbba und aca"
print(tx)
txneu = re.sub("ab*a","x",tx)
print("11: ", txneu)

# 12: Wiederholung, 1 oder mehr
txneu = re.sub("ab+a","x",tx)
print("12: ", txneu)

# 13: Wiederholung, 0 oder 1
txneu = re.sub("ab?a","x",tx)
print("13: ", txneu)

# 14: Wiederholung, m bis n
txneu = re.sub("ab{2,3}a","x",tx)
print("14: ", txneu)

# 15: Wiederholung der max. Menge von Zeichen
tx = "aa und aba und abba und aca und addda"
txneu = re.sub("a.*a","x",tx)
print("15: ", txneu)

# 16: Wiederholung der min. Menge von Zeichen
txneu = re.sub("a.*?a","x",tx)
print("16: ", txneu)

