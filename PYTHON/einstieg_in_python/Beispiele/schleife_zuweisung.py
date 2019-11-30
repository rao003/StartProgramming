import random
random.seed()
summe = 0
while (summe := summe + random.randint(1,8)) < 30:
    print("Zwischensumme:", summe)
print("Ende")




