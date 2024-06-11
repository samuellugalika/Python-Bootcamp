# creation d'une matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrice)
# affichage des elements d'une matrice
element = matrice[1][2]  # element = 6 (élément de la rangée 1, colonne 2)
# parcours d'une matrice
print(element)
for rangee in matrice:
    for element in rangee:
        print(element)

# operations sur la matrice
# Addition de deux matrices
def addition_matrices(matrice1, matrice2):
    # Vérifier si les matrices ont la même taille
    if len(matrice1) != len(matrice2) or len(matrice1[0]) != len(matrice2[0]):
        raise ValueError("Les matrices doivent avoir la même taille")

    # Initialiser la matrice résultante
    matrice_resultante = []
    for i in range(len(matrice1)):
        ligne_resultante = []
        for j in range(len(matrice1[0])):
            ligne_resultante.append(matrice1[i][j] + matrice2[i][j])
        matrice_resultante.append(ligne_resultante)

    return matrice_resultante

# Exemple d'utilisation
matrice1 = [[1, 2], [3, 4]]
matrice2 = [[5, 6], [7, 8]]
matrice_somme = addition_matrices(matrice1, matrice2)
print(matrice_somme)  # [[6, 8], [10, 12]]