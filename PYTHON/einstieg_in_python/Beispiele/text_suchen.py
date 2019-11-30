# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Anzahl Suchtexte
such = "ei"
anz = test.count(such)
print("count: Der String", such, "kommt", anz, "Mal vor")

# Erste Position des Suchtextes
anfpos = test.find(such)
print("find 1: Zum ersten Mal an Position", anfpos)

# Weitere Position des Suchtextes
nextpos = test.find(such, anfpos+1)
print("find 2: Ein weiteres Mal an Position", nextpos)

# Letzte Position des Suchtextes
endpos = test.rfind(such)
print("rfind: Zum letzten Mal an Position", endpos)

# Suchtext nicht gefunden
such = "am"
pos = test.find(such)
if pos==-1:
    print("find 3:", such, "wird nicht gefunden")
else:
    print("find 3:", such, "an Position", pos, "gefunden")

# Ersetzen von Text
test = test.replace("ist","war")
print("replace:", test)
