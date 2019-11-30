print("Umrechnung von Celsius in Fahrenheit")

# Trennung einer Zeichenkette
print("Bitte geben Sie eine"
      " Temperatur in Celsius ein: ")
TemperaturInCelsius = float(input())

# Trennung eines Ausdrucks
TemperaturInFahrenheit = TemperaturInCelsius \
                         * 9 / 5 + 32

# Trennung von Parametern
print(TemperaturInCelsius, "Grad Celsius entsprechen",
      TemperaturInFahrenheit, "Grad Fahrenheit")



