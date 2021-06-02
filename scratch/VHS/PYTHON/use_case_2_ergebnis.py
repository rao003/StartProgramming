
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

"""##### Lesen Sie die bereits gesammelten Daten in einen DataFrame. Die Daten finden Sie in der csv Datei 'EmpfehlungsSystem.csv'"""
frame = pd.read_csv("EmpfehlungsSystem.csv", header = None)
frame = pd.DataFrame(frame)

"""##### Teilen Sie dien DataFrame in features und labels. Die Labels befinden sich in der letzten Spalte, während der Rest features sind."""
features = frame[frame.columns[0:22]]
labels = frame[frame.columns[22]]
print(features.head())
print(labels.head())

"""##### Erstellen Sie den Klassifikator und trainieren Sie ihr Model."""
klassifikator = GaussianNB()
klassifikator.fit(features, labels)

"""##### Empfehlen Sie mit Hilfe Ihres Models ein Film basierent auf der Input Werte '[2,4,2,2,1,4,3,2,1,2,1,2,2,3,2,5,2,3,2,3,4,4]'. Lassen Sie sich zusätzlich noch die Wahrscheinlichkeiten für eine jede Option ausgeben."""
# Vorhersage mit Wahrscheinlichkeiten
vorhersage = klassifikator.predict([[2,4,2,2,1,4,3,2,1,2,1,2,2,3,2,5,2,3,2,3,4,4]])
vorhersageProb = klassifikator.predict_proba([[2,4,2,2,1,4,3,2,1,2,1,2,2,3,2,5,2,3,2,3,4,4]])
print(vorhersage)
print(vorhersageProb)

"""##### Visualisieren der Vorhersagewahrscheinlichkeit"""

import matplotlib.pyplot as plt

plt.pie(vorhersageProb[0])