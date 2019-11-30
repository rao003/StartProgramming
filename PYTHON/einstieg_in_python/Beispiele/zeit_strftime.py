import time
lt = time.localtime()

print(time.strftime("Tag.Monat.Jahr: %d.%m.%Y", lt))
print(time.strftime("Stunde:Minute:Sekunde: %H:%M:%S", lt))
print(time.strftime("Jahr in zwei Ziffern: %y", lt))
print(time.strftime("Tag des Jahres: %j", lt))
print()

print("Wochentag:")
print(time.strftime("Nr.(Sonntag=0): %w", lt))
print(time.strftime("Nach ISO 8601: %u", lt))
print()

print("Kalenderwoche:")
print(time.strftime("Beginn Sonntag: %U", lt))
print(time.strftime("Beginn Montag: %W", lt))
print(time.strftime("Nach ISO 8601: %V", lt))
print()

print(time.strftime("Zeitzone: %Z", lt))
