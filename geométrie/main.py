from geométrie import aire_cercle, perimetre_cercle
from geométrie import aire_rectangle, perimetre_rectangle

# Demander à l'utilisateur de choisir une forme géométrique
print("Choisissez une forme géométrique :")
print("1. Cercle")
print("2. Rectangle")
choix = input("Entrez le numéro de la forme choisie (1/2): ")

# Calculer l'aire et le périmètre en fonction du choix de l'utilisateur
if choix == '1':
    rayon = float(input("Entrez le rayon du cercle : "))
    aire = aire_cercle(rayon)
    perimetre = perimetre_cercle(rayon)
    print("Aire du cercle :", aire)
    print("Périmètre du cercle :", perimetre)
elif choix == '2':
    longueur = float(input("Entrez la longueur du rectangle : "))
    largeur = float(input("Entrez la largeur du rectangle : "))
    aire = aire_rectangle(longueur, largeur)
    perimetre = perimetre_rectangle(longueur, largeur)
    print("Aire du rectangle :", aire)
    print("Périmètre du rectangle :", perimetre)
else:
    print("Choix invalide. Veuillez choisir 1 ou 2.")

