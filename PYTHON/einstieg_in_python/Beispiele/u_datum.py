print("Tag des Datums eingeben:")
tag = int(input())
print("Monat des Datums eingeben:")
monat = int(input())
print("Jahr des Datums eingeben:")
jahr = int(input())

if tag < 1 or tag > 31:
    print("Falsches Datum")
elif monat < 1 or monat > 12:
    print("Falsches Datum")
elif monat == 4 or monat == 6 or monat == 9 or monat == 11:
    print("Letzter Tag: 30")
    if tag < 1 or tag > 30:
        print("Falsches Datum")
    else:
        print("Richtiges Datum")
elif monat == 2:
    if jahr%4 == 0 and jahr%100 != 0 or jahr%400 == 0:
        print("Letzter Tag: 29")
        if tag < 1 or tag > 29:
            print("Falsches Datum")
        else:
            print("Richtiges Datum")
    else:
        print("Letzter Tag: 28")
        if tag < 1 or tag > 28:
            print("Falsches Datum")
        else:
            print("Richtiges Datum")
else:
    print("Letzter Tag: 31")
    if tag < 1 or tag > 31:
        print("Falsches Datum")
    else:
        print("Richtiges Datum")
