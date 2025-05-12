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
print("Mot de passe généré :", mot_de_passe)
