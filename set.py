# Creation de set 
set1= {} # set vide
set2= {1,2,3, "world"} #set avec element 
set4 = {1, 2, 3}
set5= {4,5,6}
set3= set([4,5,6, "hello"]) #creation du set a partir d'une liste
print(set1, set2, set3)
# Acces aux element du set
for i in set2:
    print(i)
# verifier si un element appartient a un set
if 4 in set2:
    print("4 appartient a set2")
else:
    print("4 n'appartient pas a set2")
print(set4.issubset(set2)) #verifie que set4 est un sous-ensemble de set2 : resultat = True
#Supprimer les elements du set
set2.remove(2) # supprime 2 du set
set3.remove(4) # supprime 4 du set
# set1.remove(1) # renvoie une erreur car 1 n'est pas dans set1
print(set2, set3)
# Opérations sur les sets
union = set5 | set2  # union = {1, 3, 4, 5, 6, 'world'}
intersection = set5 & set2  # intersection = set() car il n'y a pas d'element commun dans les deux set
difference = set5 - set2  # difference = {1, 2}
difference_symetrique = set5 ^ set2  # difference_symetrique = {1, 2, 4, 5}
print(union)
print(intersection)
print(difference)
print(difference_symetrique)
# Fonctionnalités avancees sur les set
# 1. sous ensemble
set6 = {1,2,3,4}
set7 = {1,2,3,4,5,6}
if set6.issubset(set7): 
    print("Set6 est un sous-ensemble de set7")
else:
    print("Set6 n'est pas un sous-ensemble de set7")
    
# 2. supersensemble
set8 ={1,2,3,4,5}
set9 ={1,2,3,4,5,6,7}
if set9.issuperset(set8):
    print("Set8 est un super ensemble de set9")
else:
    print("Set8 n'est pas un super ensemble de set9")
