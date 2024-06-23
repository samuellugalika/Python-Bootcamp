# Exercice 1: Faire un petit script qui demandera à l'utilisateur d'entrer le nom
# d'un fichier ensuite le script genère les tables de multiplication de 1 à 12 dans
# le fichiers choisi par l'utilisateur.

with open(input("Entrer le nom du fichier a ouvrir : "), "w") as fichier:

    for n in range(1, 13):
        fichier.write("\n----------------------------------\n")
        fichier.write(f"        Table de multiplication par {n}      ")
        fichier.write("\n----------------------------------")

        for x in range(1, 13):
            z = x * n
            fichier.write(f"\n{x} x {n} = {z} ")


# Exercice 2 : Traiter le cas où le nom du fichier choisi par l'utilisateur
# existe déjà, que le script demande de
# choisir un autre nom jusqu'à ce qu'on en choisisse un qui soit different.
import os.path


def dem_nom_fichier(message):
    while True:
        nom_fichier = input(message)
        if os.path.exists(nom_fichier):
            print(f"Le fichier {nom_fichier} existe deja.\nVeuillez choisir un autre !")
        else:
            return nom_fichier


def main():
    nom_fichier = dem_nom_fichier("Entrez le nom du fichier : ")
    if nom_fichier is not None:
        print(f"Le nom du fichier choisi est : {nom_fichier}")


if __name__ == "__main__":
    main()
