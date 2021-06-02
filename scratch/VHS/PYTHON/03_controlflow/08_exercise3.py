# raiz quadrada
import math


a = 1
b = -5
c = 6

disk = b**2-4*a*c

x = (b*(-1) + math.sqrt(disk))/2*a

y = (b*(-1) - math.sqrt(b**2-4*a*c))/2*a


print(int(x))
print(int(y))

