# Zufallsgenerator
import random
random.seed()

# Initialisierung
summe = 0

# while-Schleife
while summe < 30:
    zzahl = random.randint(1,8)
    summe = summe + zzahl
    print("Zahl:", zzahl, "Zwischensumme:", summe)
    
print("Ende")




