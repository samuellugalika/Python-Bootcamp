#           Ouverture et fermeture des fichiers
fichier = open('fichier_texte.txt', 'r')  #ouverture du fichier
                                    # en mode lecture seule ('r' = read)
fichier.close()

#           Lecture des fichiers
# #lire le contenu du fichier en entier
with open('fichier_texte.txt') as fichier:
    contenu = fichier.read()
    print(contenu, '\n')

#lire une ligne dans le contenu du fichier
with open('fichier_texte.txt') as fichier:
    line = fichier.readline()
    print(line, '\n')

#lire plusieurs dans le contenu du fichier
with open('fichier_texte.txt') as fichier:
    lines = fichier.readlines()
    print(lines, '\n')

#lire le contenu du fichier ligne par ligne
with open('fichier_texte.txt', 'r') as fichier:
    for ligne in fichier:
        print(ligne, end='')

# Écriture dans un fichier
with open('fichier_texte_2.txt', 'w') as fichier:
    fichier.write("Quatrieme semaine du Python bootcamp .\n")

# Ajout à un fichier existant
with open('fichier_texte_2.txt', 'a') as fichier:
    fichier.write("Organiser par GDSC UCB.\n")

# Utilisation de with pour gérer automatiquement la fermeture du fichier
with open('fichier_texte_2.txt', 'r') as fichier:
    contenu = fichier.read()
    print('\n\n', contenu)
