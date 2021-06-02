# ungerade

numero1 = int(input ("Enter your firstNumber"))
numero2 = int(input ("Enter your secondNumber"))

summe = 0
for x in range(numero1,numero2):
    if (x%2 != 0):
        print(x)
        summe = summe + x

print(summe)


# nicht optimiert
