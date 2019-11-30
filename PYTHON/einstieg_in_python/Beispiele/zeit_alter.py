# Modul time
import time

# Geburtstag
dztupel = 1979, 5, 7, 0, 0, 0, 0, 0, 0
print("Geburt:", time.strftime("%d.%m.%Y", dztupel))
geburt = time.mktime(dztupel)
ltgeburt = time.localtime(geburt)

# Aktuell
ltheute = time.localtime()
print("Heute:", time.strftime("%d.%m.%Y"))

# Alter berechnen
alter = ltheute[0] - ltgeburt[0]
if ltheute[1] < ltgeburt[1] or \
         ltheute[1] == ltgeburt[1] and \
         ltheute[2] < ltgeburt[2]:
    alter = alter - 1
print("Alter:", alter)
