
numero = int(input ("Enter your firstNumber"))

y = 1
x = 1
z = 0

while z < numero:
    z = y + x
    y = x
    x = z
    print (z)


