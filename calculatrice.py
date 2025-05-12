# Notre fichier calculatrice.py contient des fonctions pour les opérations de base addition, soustraction, multiplication et division.
def addition(a, b):
    return a +b
def soustraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        print("Erreur: Division par zéro")
        return None
    else:
        return a / b
