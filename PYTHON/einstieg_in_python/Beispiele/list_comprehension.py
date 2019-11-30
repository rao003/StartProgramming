# Zwei Beispiellisten
xliste = [3, 6, 8, 9, 15]
print(xliste)
yliste = [2, 13, 4, 8, 4]
print(yliste)
print()

# Beispiel 1: Version ohne List Comprehension
aliste = []
for item in xliste:
    aliste.append(item+1)
print(aliste)

# Beispiel 1: Version mit List Comprehension
aliste = [item + 1 for item in xliste]
print(aliste)
print()

# Beispiel 2: Version ohne List Comprehension
bliste = []
for item in xliste:
    if item > 7:
        bliste.append(item + 1)
print(bliste)

# Beispiel 2: Version mit List Comprehension
bliste = [item + 1 for item in xliste if item > 7]
print(bliste)
print()

# Beispiel 3: Version ohne List Comprehension
cliste = []
for i in range(len(xliste)):
    if xliste[i] < 10 and yliste[i] < 10:
        cliste.append(xliste[i]*10 + yliste[i])
print(cliste)

# Beispiel 3: Version mit List Comprehension
cliste = [xliste[i]*10 + yliste[i]
          for i in range(len(xliste))
          if xliste[i] < 10 and yliste[i] < 10]
print(cliste)
