tname = "Robinson Crusoe"

try:
    tname[3] = "e"
except:
    print("Fehler")

try:
    tname[3:5] = "el"
except:
    print("Fehler")
