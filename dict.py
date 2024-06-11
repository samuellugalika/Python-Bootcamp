# Creation du dictionnaire
mon_dict1 = {} #dictionnaire vide
mon_dict2 = {"Nom" : "Samuel", "Age" : 100, "Pays" : "RDC"} #dictionnaire avec element
# Creation du dictionnaire a partir d'une liste de paire cle-valeur
mon_dict3 = dict([("Ville","Bukavu"), ("Numero" , 23), ("Nom" , "Luc")])
print(mon_dict1)
print(mon_dict2)
print(mon_dict3)
# acces aux elements du dictionnaire
nom = mon_dict2["Nom"] #affiche la valeur de "Nom"
Pays = mon_dict2["Pays"]  #affiche la valeur de "Pays"
# ville = mon_dict2["Goma"] #provoque une erreur car "Goma" est absent dans mon_dict2
print(nom, Pays)
# ajout, suppression et modification des element du dictionnaire
mon_dict2["ville"] = "Goma" #ajoute la paire cle-valeur ville et goma
print(mon_dict2)
mon_dict2["Age"] = 20 # modifie la valeur de la paire cle-valeur age
print(mon_dict2)
del mon_dict2["Pays"] #supprime la paire cle-valeur Pays
print(mon_dict2)
# parcourir les elements du dictionnaire
# 1 parcourir les cle du dictionnaire
for cle in mon_dict2.keys():
    print(cle)  #nom, age , ville
# 2 parcourir les valeurs du dictionnaire
for valeur in mon_dict2.values():
    print(valeur) #sam, 20, goma
# 2 parcourir les cles et les valeurs du dictionnaire
for cle, valeur in mon_dict2.items():
    print(cle, valeur)
# fonctionnalites avancees sur les dictionnaires
# 1 Nesting dictionaries (dictionnaire dans dictionnaire)
etudiants = {
    "Sam": {"cours":["Math", "francais"], "not_moy" : 20},
    "Franck": {"cours":["Info", "droit"], "not_moy" : 18}
}
note_sam_math = etudiants["Sam"]["cours"][0]  # note_sam_math = "Math"
note_franck_droit = etudiants["Franck"]["not_moy"]  # note_franck_droit = 18
print(note_sam_math)
print(note_franck_droit)
# 2 Utilisation des Dictionnaires comme Valeurs par Défaut
def get_note_etudiant(nom_etudiant, cours):
  notes_etudiants = {"Alice": {"Mathématiques": 90, "Informatique": 85},
                     "Prince": {"IRS": 75, "Chimie": 82}}
  return notes_etudiants.get(nom_etudiant, {}).get(cours, -1)

note_alice_math = get_note_etudiant("Alice", "Mathématiques")  # note_alice_math = 90
note_prince_histoire = get_note_etudiant("Prince", "Histoire")  # note_prince_histoire = -1 (cours inexistant)
print(note_alice_math)
print(note_prince_histoire)
# 3 comparaison et tri des dictionnaire
dictionnaire1 = {"nom": "Alice", "age": 30}
dictionnaire2 = {"nom": "Bob", "age": 30}
dictionnaire1 == dictionnaire2  # False (les clés sont différentes)
dictionnaire1["age"] = 31
dictionnaire1 == dictionnaire2  # True (les clés et les valeurs sont identiques)
# 4 copier et fusionner les dictionnaire
dictionnaire_original = {"nom": "Alice", "age": 30}
# Copie par référence
copie_par_reference = dictionnaire_original #attribue la valeur du dict original a copie par reference
copie_par_reference["ville"] = "Paris" #ajoute par reference au dict original la paire cle-valeur ville
print(copie_par_reference) 
# Copie par méthode
copie_par_methode = dictionnaire_original.copy() #copie le dict original 
copie_par_methode["profession"] = "Développeuse" #ajoute par reference au dict original la paire cle-valeur profession
print(copie_par_methode)
# Fusion de dictionnaires
dictionnaire_fusionne = dict(dictionnaire_original, **copie_par_methode) #fusionne le dictionnaire original et la copie par methode
print(dictionnaire_fusionne)