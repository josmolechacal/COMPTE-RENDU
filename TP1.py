""" 1.Écrire un programme, qui définit 3 variables : une variable de type texte, une 
variable de type nombre entier, une variable de type nombre décimal et qui 
affiche leurs valeurs et leurs types."""

text = 'Yoan'
print(text)
print(type(text)) # Affiche le type string

entier = 10
print(entier)
print(type(entier)) # Affiche le type int

float = 25.5
print(float)
print(type(float)) # Affiche le type float

"""  2.Affecter dans une même ligne les 3 variables précédemment définies."""
liste  = [text, entier, float] ## On Crée une liste avec des types différents
print(liste)

"""3.Écrire un programme qui, à partir d’un rayon et d’une hauteur donnés, calcule
 le volume d’un cône droit : V = 1/3×π×r²×h"3"""
from math import *
r = input("entrer une valeur du rayon \n")
float(r)
h = input("entrer une valeur du hauteur \n")
float(h)
V = 1/3 * (pi * float(r)**2 * float(h))
print("le rayon est", r, "cm")
print("la hauteur est ", h, "cm")
print("le volume V du cone est", V, "cm³")


""" 3.Écrire un programme qui affiche le type du résultat des instructions suivantes 
a=3 et a==3 """
a=3
print(type(a))

a==3
print(type(a))


""" 4. Écrire un programme, qui ajoute une chaîne de caractères à un nombre entier
 (Exemple la chaîne ”le chat” et le nombre 3 pour donner le chat + 3)"""
chaine = "le chat"
entier = 3
resultat = chaine + "+" + str(entier) # Concatène une chaîne et un nombre
print(resultat)