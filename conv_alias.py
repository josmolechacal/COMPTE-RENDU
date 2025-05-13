# Import avec alias
import conversion as conv

print("\nBienvenue dans le module de conversion !")
print("-------------------------------------------")

celsius = conv.fahrenheit_vers_celsius(150.6)
fahrenheit = conv.celsius_vers_fahrenheit(17)
pi = conv.PI
gravite = conv.GRAVITE

print("\nLa température de 98.6°F est équivalente à", celsius, "°C")
print("\nLa température de 37°C est équivalente à", fahrenheit, "°F")
print("\nLa valeur de PI est :", pi)
print("\nLa valeur de la gravité est :", gravite)

