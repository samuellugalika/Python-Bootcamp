# le tranchage
# la liste personnes = ['GAbriel', 'Bienfait', 'Janvier', 'Faustin']
# fruits = ["banane", "pomme", "orange", "fraise", "kiwi"]
personnes = ["Faustin", "Joseph", "Bienvenue", "David"]
sous_liste1 = personnes[1:3]  # ['Bienfait', 'Janvier']  # Du deuxième au troisième élément (exclusif)
sous_liste2 = personnes[-2:]  # ['Janvier', 'Faustin']  # Du deuxième élément de la fin jusqu'à la fin
sous_liste3 = personnes[::2]  # ['GAbriel', 'Janvier']  # Prend tous les éléments avec un pas de 2
print(sous_liste1)
print(sous_liste2)
print(sous_liste3)

# la concaténation
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste_combinee = liste1 + liste2  # [1, 2, 3, 4, 5, 6]
print(liste_combinee)

# le filtrage
# Filtrons la liste combinée, liste_combinee = [1, 2, 3, 4, 5, 6]
def est_pair(nombre):
    return nombre % 2 == 0


liste_nombres_pairs = list(filter(est_pair, liste_combinee))  # output est [2, 4, 6]
print(liste_nombres_pairs)