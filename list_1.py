# Création d'une liste vide
ma_liste = []
print(ma_liste)
# Creation d'une liste
fruits = ["banane", "pomme", "orange"]
print(fruits)
# Accès à un élément par son index
premier_fruit = fruits[0]  # premier élément dans le variable fruits est "banane"
print(premier_fruit)
# Modification d'un élément
fruits[1] = "poire"  # La pomme est remplacée par une poire
print(fruits)
# Ajout d'un élément
fruits.append("épices")  # "épices" est ajouté à la fin de la liste
print(fruits)
# Suppression d'un élément
fruits.remove("orange")  # "orange" est supprimé de la liste
print(fruits)
# Longueur de la liste
nombre_fruits = len(fruits)
print(nombre_fruits)