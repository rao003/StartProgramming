# Modul time
import time

# Zwei Zeitangaben erzeugen
dztupel1 = 2019, 12, 15, 23, 55, 0, 0, 0, 0
damals1 = time.mktime(dztupel1)
print("Zeit 1:", time.strftime("%d.%m.%Y %H:%M:%S",
                               dztupel1))

dztupel2 = 2019, 12, 16, 0, 5, 15, 0, 0, 0
damals2 = time.mktime(dztupel2)
print("Zeit 2:", time.strftime("%d.%m.%Y %H:%M:%S",
                               dztupel2))
print()

# Differenz berechnen
print("Differenz:")

diff_sek = damals2 - damals1
print(diff_sek, "Sekunden")

diff_min = diff_sek/60
print(diff_min, "Minuten")

diff_std = diff_min/60
print(diff_std, "Stunden")

diff_tag = diff_std/24
print(diff_tag, "Tage")
