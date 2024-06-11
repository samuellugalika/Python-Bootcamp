# operations sur les tuples
"""La comparaison entre deuxx tuples"""
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

if tuple1 == tuple2:
    print("Les tuples sont égaux")
else:
    print("Les tuples sont différents")

"""L'appartenance"""
if 2 in tuple1:
    print("2 est dans le tuple")
else:
    print("2 n'est pas dans le tuple")

"""Longueur d'un tuple"""
longueur = len(tuple1)
print(longueur)

"""Concrétion d'un tuple"""
liste1 = list(tuple1)  # liste1 = [1, 2, 3]
print(liste1)

# tuples imbriqué
tuple1 = (1, 2, (3, 4))
# Accéder à l'élément imbriqué
element_imbrique = tuple1[2][1]  # element_imbrique = 4
print(element_imbrique)
