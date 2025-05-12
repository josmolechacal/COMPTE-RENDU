""" 1-Écrire un programme liste_animaux.py, qui initialise la liste et 
l’affiche.  Afficher ensuite le premier et le troisième élément de 
la liste seulement.  liste_animaux = ["lapin"," tigre", "dragon", "poule"] """

list_animaux = ["lapin", "tigre", "dragon", "poule"]
print(list_animaux)  #Affiche la liste complète
print(list_animaux[0],",",list_animaux[2]) ## Affiche des éléments spécifiques 

"""2. Inverser la liste puis afficher le premier et le troisième élément."""
list_animaux.reverse() # Inverse la liste in-place
print(list_animaux) 
print(list_animaux[0],",",list_animaux[2])


""""3. Ajouter l’élément lion à la fin de la liste (append). """
list_animaux.append('lion') # Ajoute à la fin
print(list_animaux)

""""4. Supprimer l’élément d’indice 3. Supprimer ensuite l’ensemble 
des animaux domestiques """
del list_animaux[3] # Supprime par indice
print(list_animaux)

## Avec la fontion remove on supprime un seul animal domestique la poule et vue qu'on a déjà supprimer le lapin 
## On print tout simplement une liste d'animaux elle ne contiendra plus le lapin et la poule 
list_animaux.remove('poule')  # Supprime par valeur
print(list_animaux)



""""5. Afficher le nombre de caractères du deuxième élément de la liste 
comme suit : lapin possède 5 caractères """
print(f"\n{list_animaux[1]} possède {len(list_animaux[1])} caractères")


"""6. Puister mouton dans le deuxième élément de la liste (insert), puis 
supprimer l’ensemble des animaux domestiques """

list_animaux.insert(1, "mouton") # Insertion d'un élément
print("Liste des animaux après insertion de mouton: ", list_animaux)

#Filtrage des animaux domestiques
animaux_domestiques = ["lapin", "poule","mouton"]  
list_animaux = [animal for animal in list_animaux if animal not in animaux_domestiques] 
print("Liste sans des animaux domestiques: ", list_animaux)


"""7. Créer une deuxième liste qui contient deux éléments vache et 
oiseau puis faire l’addition des deux listes et multiplication de la 
deuxième liste par 2, """
### Addition des deux listes 
list_animaux2 = ["vache","oiseau"]
list_addition = list_animaux + list_animaux2
print("Addition des deux listes: ", list_addition)

### Multiplication de deux listes 
list_multiplie = list_animaux2 * 2
print("Multiplicationn de la liste2: ", list_multiplie)

"""8. Copier une liste dans une autre liste_copie puis afficher 
les éléments contenant les animaux domestiques de la 
liste_copie."""

### Copie de la liste addition dans list_copie
list_copie = list_addition.copy()
print(list_copie)

### Afficher les éléments contenant les animaux domestiques de la list_copie
animaux_domestiques = ["lapin","poule","vache","oiseau"]
animaux_domestiques_copie = [animal for animal in list_copie if animal in animaux_domestiques]
print("Animaux domestique dans la liste copiée \n", animaux_domestiques_copie)



















