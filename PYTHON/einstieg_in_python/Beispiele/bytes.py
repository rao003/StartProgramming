# Datentyp str
st = "Hallo"
print(st, type(st))

# Datentyp bytes
by = b'Hallo'
print(by, type(by))

# Umwandlung von str in bytes
by = bytes("Hallo", "UTF-8")
print(by, type(by))

# Umwandlung von bytes in str
by = b'Hallo'
st = by.decode()
print(st, type(st))
