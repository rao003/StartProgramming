# fizz buzz


numero = int(input ("Enter your firstNumber"))

while(True):
    if numero == 0:
        print("ende")
        exit()
    elif (numero%3 == 0 and numero%5 == 0):
        print("fizzbuzz")
    elif numero%5 == 0 :
        print("buzz")
    elif numero%3 == 0 :
        print("fizz")
    else:
        print("echo", numero)

#  korrekt 
