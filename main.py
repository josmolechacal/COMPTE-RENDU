from geometrie.cercle import aire as aire_cercle, perimetre as perimetre_cercle
from geometrie.rectangle import aire as aire_rectangle, perimetre as perimetre_rectangle

# Demander à l'utilisateur de choisir une forme géométrique
print("\nChoisissez une forme géométrique :")
print("\n1. Cercle")
print("\n2. Rectangle")
choix = input("\nEntrez le numéro de la forme choisie (1/2): ")

# Calculer l'aire et le périmètre en fonction du choix de l'utilisateur
if choix == '1':
    rayon = float(input("\nEntrez le rayon du cercle : "))
    aire = aire_cercle(rayon)
    perimetre = perimetre_cercle(rayon)
    print("\nAire du cercle :", aire, "cm²")
    print("\nPérimètre du cercle :", perimetre, "cm")
elif choix == '2':
    longueur = float(input("\nEntrez la longueur du rectangle : "))
    largeur = float(input("\nEntrez la largeur du rectangle : "))
    aire = aire_rectangle(longueur, largeur)
    perimetre = perimetre_rectangle(longueur, largeur)
    print("\nAire du rectangle :", aire, "m²")
    print("\nPérimètre du rectangle :", perimetre, "m")
else:
    print("\nChoix invalide. Veuillez choisir 1 ou 2.")

