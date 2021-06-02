"""
input

dividido por 4 e gerade

nao pode ser dividido por 100

mas se for dividido por 400 e gerade 

"""

year = int(input ("Enter your year"))

if (year % 4 == 0) or (year % 100 !=0) and (year % 400 ==0)  :
    print("leapyear")
else:
    print("not")



