dateiName = "/sys/class/thermal/thermal_zone0/temp"
datei = open(dateiName, "r")
tp = datei.readline()
tp = int(tp) / 1000
datei.close()
print("CPU-Temperatur:", tp, "Grad Celsius")
