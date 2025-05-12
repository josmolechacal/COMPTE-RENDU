"""#Exercice 1 : Générateur de mot de passe
import random
import string

def generate_password(longueur):
    miniscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    caracteres_speciaux = string.punctuation
    

# Combinaison de tous les caractères
    combinaison = miniscules + majuscules + chiffres + caracteres_speciaux

# Génération du mot de passe
    Password = [
        random.choice(miniscules), 
        random.choice(majuscules),
        random.choice(chiffres),
        random.choice(caracteres_speciaux)
    ]

    # Compléter le reste du mot de passe
    for _ in range(longueur - 4):
        Password.append(random.choice(combinaison))
    # On mélange le mot de passe pour le rendre plus aléatoire
    random.shuffle(Password)
    # On convertit la liste en chaîne de caractères
    mot_de_passe = ''.join(Password)
    return mot_de_passe

# On affiche le mot de passe généré
print("\nBienvenue dans le générateur de mot de passe !")
print("\nLe mot de passe généré contiendra au moins une lettre minuscule, une lettre majuscule, un chiffre et un caractère spécial.")
print("-----------------------------------------------------------------------------------------------------------------------------")
# On demande à l'utilisateur de saisir la longueur du mot de passe
print("\nVeuillez entrer la longueur du mot de passe souhaitée (minimum 5 caractères) :")
longueur = int(input("\nEntrez la longueur du mot de passe : "))
mot_de_passe = generate_password(longueur)
print("Le mot de passe généré est de longueur", longueur)
# On affiche le mot de passe généré
print("Mot de passe généré :", mot_de_passe)"""

"""#Exercice 2 : Gestion de date et de l'heure
from datetime import datetime, timedelta


print("\nBienvenue dans le gestionnaire des dates et d''heure !")
print("--------------------------------------------------------")
# la date actuelle 
date_actuelle = datetime.now()
# Afficher la date actuelle au format jj/mm/aaaa
date_actuelle_str = date_actuelle.strftime("%d/%m/%Y")
print("\nLa date actuelle est :", date_actuelle_str)

# Afficher le jour de la semaine
jour_semaine = date_actuelle.strftime("%A")
print("\nAujourd'hui, c'est :", jour_semaine)

# Afficher la date dans 30 jours 
date_dans_30_jours = date_actuelle + timedelta(days=30) 
date_dans_30_jours_str = date_dans_30_jours.strftime("%d/%m/%Y")
print("\nDans 30 jours, nous serons le :", date_dans_30_jours_str)

# Afficher la différence entre deux dates saisises par l'utilisateur 
date1_str = input("Entrez la première date (jj/mm/aaaa) : ")
date2_str = input("Entrez la deuxième date (jj/mm/aaaa) : ")
date1 = datetime.strptime(date1_str, "%d/%m/%Y")
date2 = datetime.strptime(date2_str, "%d/%m/%Y")
difference = abs((date2 - date1).days)
print('\nLa différence entre les deux dates est de: ', difference, 'jours')"""


#Exercice 3 : Création d'un module simple de calculatrice

# dans ce fichier, importons le module calculatrice et utilisons ses fonctions
import calculatrice

# On affiche un message de bienvenue
print("\nBienvenue dans la calculatrice !")
print("--------------------------------")

# On demande à l'utilisateur de choisir une opération
print("\nChoisissez une opération :")
print("\n1. Addition")
print("\n2. Soustraction")
print("\n3. Multiplication")
print("\n4. Division")
choix = input("\nEntrez le numéro de l'opération souhaitée (1/2/3/4): ")

# On demande à l'utilisateur de saisir deux nombres
a = float(input("\nEntrez le premier nombre : "))
b = float(input("\nEntrez le deuxième nombre : "))

# On effectue l'opération choisie
if choix == '1':
    print("\nLe résultat de l'addition est :", calculatrice.addition(a, b))
elif choix == '2':
    print("\nLe résultat de la soustraction est :", calculatrice.soustraction(a, b))
elif choix == '3':
    print("\nLe résultat de la multiplication est :", calculatrice.multiplication(a, b))
elif choix == '4':
    print("\nLe résultat de la division est :", calculatrice.division(a, b))
else:
    print("\nErreur: Opération non valide")

# On affiche un message de fin  
print("\nMerci d'avoir utilisé la calculatrice !")
# On affiche un message de fin
print("--------------------------------------------------------")

# Exercice 4 : Organisation d'un module 

#1 création d'un module géométrie avec deux sous-modules : cercle et rectangle
#2 Dans chaque sous-module, on définit des fonctions pour calculer l'aire et le périmètre
#3 Importez et utiliser ses fonctions depuis un fichier principal
