# Funktion
def chg(v, zk, li, di, st):
    v = 8
    zk = "ciao"
    li[0] = 7
    di["x"] = 7
    st.discard(3)

    # lokale Ausgabe
    print("In Funktion:")
    print(v, zk)
    print(li, di, st)

# Startwerte
hv = 3
hli = [3,"abc"]
hzk = "hallo"
hdi = {"x":3, "y":"abc"}
hst = set([3, "abc"])

# Ausgabe vorher
print("vorher:")
print(hv, hzk)
print(hli, hdi, hst)

# Aufruf der Funktion
chg(hv, hzk, hli, hdi, hst)

# Ausgabe nachher
print("nachher:")
print(hv, hzk)
print(hli, hdi, hst)
