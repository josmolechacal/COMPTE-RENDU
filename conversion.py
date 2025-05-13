# Création du module conversion.py
PI = 3.14159
GRAVITE = 9.81

# Fonction de conversion Celsius vers Fahrenheit et vice versa
def fahrenheit_vers_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9) #round() arrondit le résultat à l'entier le plus proche
def celsius_vers_fahrenheit(celsius):
    return round((celsius * 9/5) + 32)

