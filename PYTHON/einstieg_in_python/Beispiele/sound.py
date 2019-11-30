import winsound, time

# Folge von Tönen mit unterschiedlicher Frequenz
for i in range (600, 1500, 200):
    print(i)
    winsound.Beep(i, 500)
    time.sleep(0.2)

# Beispiel für Systemton
print("SystemQuestion")
winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

# Beispiel für WAV-Datei
print("GAkkord.wav")
winsound.PlaySound("GAkkord.wav", winsound.SND_FILENAME)
