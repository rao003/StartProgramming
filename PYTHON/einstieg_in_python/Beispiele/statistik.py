import statistics

# Mittelwerte einer Liste
probe1 = [5, 2, 4, 17]
print("Arithmetischer Mittelwert:", statistics.mean(probe1))
print("Geometrischer Mittelwert:",
    statistics.geometric_mean(probe1))
print("Harmonischer Mittelwert:",
    statistics.harmonic_mean(probe1))
print()

# Median
print("Median:", statistics.median(probe1))
probe2 = [5, 2, 4, 17, 3]
print("Median:", statistics.median(probe2))
print()

# Unterer Median
print("Unterer Median:", statistics.median_low(probe1))
print("Unterer Median:", statistics.median_low(probe2))
print()

# Oberer Median
print("Oberer Median:", statistics.median_high(probe1))
print("Oberer Median:", statistics.median_high(probe2))
print()

# Modus
probe3 = [3, 5, 5, 12, 17, 17]
print("Modus:", statistics.mode(probe3))
print("Multimodus:", statistics.multimode(probe3))
print()

# Tupel, Werte eines Dictionary
probe4 = 5, 2, 4, 17
print("aus Tupel:", statistics.mean(probe4))
probe5 = {'D':5, 'NL':2, 'CH':4, 'F':17}
print("aus Dictionary:", statistics.mean(probe5.values()))
