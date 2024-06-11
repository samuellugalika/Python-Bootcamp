# Création d'une liste avec des valeurs initiales qui sont les noms des personnes arrivaient à temps
personnes = ["Faustin", "Joseph", "Bienvenue", "David"]
# Autre création des listes
nombres = [1, 2, 3, 4, 5]
melange = ["pomme", 10, True]
print(personnes, melange, nombres)
# Accéder au premier élément de la liste personnes
premier_personne = personnes[0]  # premier_personne = "Faustin"
print(premier_personne)
# Accéder au dernier élément de la liste personnes
dernier_personne = nombres[-1]  # dernier_personnes = "David"
print(dernier_personne)
# Accéder à un élément par son index négatif
avant_dernier_personnes = personnes[-2]  # avant_dernier_personnes = "Bienvenue"
print(avant_dernier_personnes)
personnes[1] = ("Bienfait" ) # Remplace "Joseph" par "Bienfait" à l'index 1 de la liste personne
personnes.append("Gabriel")  # Ajoute "GAbriel" à la fin de la liste personnes
personnes.remove("David")  # Supprime "David" de la liste personnes
personnes.pop(2)  # Supprime l'élément à l'index 2 (le troisième élément qui est Bienvenue)
personnes.insert(1, "Janvier")  # Insère "Janvier" avant "Bienfait" (index 1)
personnes.reverse()  # Renverser les éléments de la liste de leur place
print(personnes)
# Parcourir une liste 
numero = 1
for personne in personnes:
    print(f"Personne N°{numero}", personne)  # Affiche chaque personne de la liste
    numero += 1