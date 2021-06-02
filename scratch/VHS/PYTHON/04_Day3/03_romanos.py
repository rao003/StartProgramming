""""

numeros romanos

1 I
2 II
3 III
4 IV
5 V
6 VI
7 VII
8 VIII
9 IX
10 X

"""""
A = "I"
B = "V"
C = "X"

number = int(input ("Enter your number"))

if number in range(0,3):
    print (number*A)
elif number == 4:
    print (A+B)
elif number == 5:
    print (B)
elif number in range(6,9):
    print (B+(number-5)*A)
elif number == 9:
    print (A+C)
elif number == 10:
    print (C)    
else:
    print( "have a nice day")  #TODO: more

